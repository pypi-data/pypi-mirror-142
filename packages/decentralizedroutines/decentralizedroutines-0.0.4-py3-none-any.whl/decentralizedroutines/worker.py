# implements a decentralized routines worker 
# connects to worker pool
# broadcast heartbeat
# listen to commands


from cProfile import run
import os,sys,psutil,time,json,boto3,subprocess

from numpy import require
from multiprocessing.pool import ThreadPool

from concurrent.futures import process, thread
from pathlib import Path

from SharedData.Logger import Logger
logger = Logger(__file__)

from SharedData.SharedDataAWSKinesis import KinesisStreamConsumer,KinesisStreamProducer

def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """
    Logger.log.info('restarting worker...')
    try:
        p = psutil.Process(os.getpid())
        children = p.children(recursive=True)
        for child in children:
            child.kill()                   
    except Exception as e:
        Logger.log.error(e)

    python = sys.executable
    os.execl(python, python, *sys.argv)

def send_command(command,env=None):
    Logger.log.debug('sending command: %s...' % (' '.join(command)))

    if env is None:
        process = subprocess.Popen(command,\
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,\
            universal_newlines=True, shell=True)        
    else:    
        process = subprocess.Popen(command,\
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,\
            universal_newlines=True, shell=True,env=env)        

    while True:
        output = process.stdout.readline()
        if ((output == '') | (output == b''))\
                & (process.poll() is not None):
            break        
        if (output) and not (output.startswith('Completed')):
            if output.rstrip()!='':
                Logger.log.debug('command response:'+output.rstrip())  
    rc = process.poll() #block until process terminated
    success= rc==0
    if success:
        Logger.log.debug('sending command DONE!')
        return True
    else:
        Logger.log.debug('sending command ERROR:%s!' % (''.join(process.stderr.readlines())))
        return False

GIT_TOKEN='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'
GIT_URL='https://'+GIT_TOKEN+'@github.com/jcarlitooliveira/'
stream_name='deepportfolio-workerpool'
profile_name='kinesis-logs-write-only'
username=os.environ['USERNAME']+'@'+os.environ['COMPUTERNAME']
repo_folder=os.environ['USERPROFILE']+'\\src\\'

Logger.log.info('Starting worker %s' % (username))

routines = []
consumer = KinesisStreamConsumer(stream_name, profile_name)
producer = KinesisStreamProducer(stream_name, profile_name)

while True:
    for proc in routines:
        if proc.poll() is not None:
            routines.remove(proc)
 
    consumer.consume()
    for record in consumer.stream_buffer:    
        print('Received:'+str(record))    
        
        command = record
        if ('job' in command) & ('target' in command):
            if ((command['target']==username) | (command['target']=='ALL')):
                if command['job'] == 'command':
                    
                    data = {                
                        'sender' : username,
                        'response': 'command sent',
                        'command' :command['command'],
                    }
                    producer.produce(data,'response')

                    send_command(command['command'])
                
                elif command['job'] == 'routine':
                    Logger.log.info('Running routine %s/%s' % (command['repo'],command['routine']))

                    repo_path=Path(repo_folder)/command['repo']
                    requirements_path = repo_path/'requirements.txt'
                    python_path=repo_path/'venv\\Scripts\\python.exe'
                    
                    repo_exists = repo_path.is_dir()
                    venv_exists = python_path.is_file()
                    install_requirements=~python_path.is_file()                    
                    runroutine = False

                    env = os.environ.copy()
                    env['VIRTUAL_ENV'] = str(repo_path/'venv')
                    env['PATH'] = str(repo_path/'venv')+';'+str(repo_path/'venv\\Scripts')
                    env['PYTHONPATH'] = str(repo_path/'venv')+';'+str(repo_path/'venv\\Scripts')
                    
                    # GIT PULL OR GIT CLONE
                    if repo_exists:                 
                        Logger.log.info('Pulling repo %s/%s' % (command['repo'],command['routine']))    
                        requirements_lastmod = 0
                        if requirements_path.is_file():
                            requirements_lastmod = os.path.getmtime(str(requirements_path))
                        # pull existing repo   
                        cmd = ['git','-C',str(repo_path),'pull']                        
                        if not send_command(cmd):
                            Logger.log.error('running routine %s/%s ERROR:could not pull repo!'\
                                 % (command['repo'],command['routine']))
                            runroutine = False
                        else:
                            install_requirements = os.path.getmtime(str(requirements_path))!=requirements_lastmod
                            runroutine=True                            
                    else:                        
                        Logger.log.info('Cloning repo %s/%s' % (command['repo'],command['routine']))
                        cmd = ['git','-C',str(repo_path.parents[0]),\
                            'clone',GIT_URL+command['repo']]                                   
                        if not send_command(cmd):
                            Logger.log.error('running routine %s/%s ERROR:could not clone repo!'\
                                 % (command['repo'],command['routine']))
                            runroutine=False
                        else:               
                            runroutine=True

                    # CREATE VENV
                    if (runroutine) & (not venv_exists):
                        Logger.log.info('Creating venv %s/%s' % (command['repo'],command['routine']))
                        if not send_command(['python','-m','venv',str(repo_path/'venv')]):
                            Logger.log.error('running routine %s/%s ERROR:could not create venv!'\
                                % (command['repo'],command['routine']))
                            runroutine=False
                        else:
                            runroutine=True
                    
                    # INSTALL REQUIREMENTS
                    if (runroutine) & (install_requirements):
                        Logger.log.info('Installing requirements %s/%s' % (command['repo'],command['routine']))
                        if not send_command([str(python_path),'-m','pip','install','-r',str(requirements_path)],env=env):
                            Logger.log.error('running routine %s/%s ERROR:could not install requirements!'\
                                % (command['repo'],command['routine']))
                            runroutine=False
                        else:
                            Logger.log.debug('repo installed %s/%s!'\
                                % (command['repo'],command['routine']))
                            runroutine=True
                                        
                    # RUN ROUTINE 
                    if runroutine:
                        Logger.log.info('Starting process %s/%s' % (command['repo'],command['routine']))
                        env = os.environ.copy()
                        env['VIRTUAL_ENV'] = str(repo_path/'venv')
                        env['PATH'] = str(repo_path/'venv')+';'+str(repo_path/'venv\\Scripts')+';'+env['PATH']
                        env['PYTHONPATH'] = str(repo_path/'venv')+';'+str(repo_path/'venv\\Scripts')
                        cmd = [str(repo_path/'venv\\Scripts\\python.exe'),str(repo_path/command['routine'])]                        
                        proc = subprocess.Popen(cmd,env=env)                        
                        routines.append(proc)    

                elif command['job'] == 'status':    
                    Logger.log.info('Running %i process' % (len(routines)))
                    for proc in routines:
                        Logger.log.info('Process id %i' % (proc.pid))
                elif command['job'] == 'restart':                    
                    restart_program()                
                elif command['job'] == 'ping':
                    Logger.log.info('pong')
                elif command['job'] == 'pong':
                    Logger.log.info('ping')

    consumer.stream_buffer = []
    time.sleep(1)

    