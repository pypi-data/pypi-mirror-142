# implements a decentralized routines master 
# connects to worker pool
# broadcast heartbeat
# listen to commands


from distutils.log import Log
import os,time,json,boto3
from concurrent.futures import thread


from SharedData.Logger import Logger
logger = Logger(__file__)
from SharedData.SharedDataAWSKinesis import KinesisStreamConsumer,KinesisStreamProducer


stream_name='deepportfolio-workerpool'

profile_name='kinesis-logs-write-only'
username=os.environ['USERNAME']+'@'+os.environ['USERDOMAIN']

Logger.log.info('Starting master')
session = boto3.Session(profile_name=profile_name)
client = session.client('kinesis')

# #create stream
# try:
#     response = client.create_stream(
#         StreamName=stream_name,
#         ShardCount=1,
#         StreamModeDetails={
#             'StreamMode': 'PROVISIONED'
#         }
#     )
#     Logger.log.info('Kinesis Stream %s created!' % (stream_name))
# except Exception as e:
#     pass

consumer = KinesisStreamConsumer(stream_name, profile_name)
producer = KinesisStreamProducer(stream_name, profile_name)

# TODO FIX ERROR
#Rate exceeded for shard shardId-000000000000 

target='jcooloj@500010349783-NB'

target='jcooloj@TRADEBOT01-PC'
target='jcooloj@TRADEBOT03-PC'
target='jcooloj@TRADEBOT04-PC'
target='jcooloj@TRADEBOT05-PC'
target='jcooloj@TRADEBOT06-PC'
target='jcooloj@TRADEBOT07-PC'
target='Administrator@IP-10-68-244-22'
target='ALL'

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "ping",    
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "pong",    
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "status",    
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['wmic','path','win32_VideoController',\
        'get','name,deviceID,Status'],
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'Backtest-RiskMetrics',
    "routine" : "calculate_moments_cpu.py"
}
producer.produce(data,'command')


data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'MarketData-Bloomberg',
    "routine" : "producer.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'Backtest-RiskMetrics',
    "routine" : "realtimeprice.py"
}
producer.produce(data,'command')


data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'MarketData-CSIData',
    "routine" : "update.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'MarketData-CSIData',
    "routine" : "download.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'MarketData-CSIData',
    "routine" : "load.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'MarketData-Bloomberg',
    "routine" : "producer.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'SharedData',
    "routine" : "tests\\test08_logconsumer.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ["git","pull"]
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['venv\\Scripts\\python.exe','-m',\
        'pip','install','-r','requirements.txt']
}
producer.produce(data,'command')


data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['shutdown','-f','-r']
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "restart",
}
producer.produce(data,'command')

# response = client.delete_stream(
#     StreamName=stream_name
# )


