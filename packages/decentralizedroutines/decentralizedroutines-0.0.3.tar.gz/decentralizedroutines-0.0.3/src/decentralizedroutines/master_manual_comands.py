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


#create stream
try:
    response = client.create_stream(
        StreamName=stream_name,
        ShardCount=1,
        StreamModeDetails={
            'StreamMode': 'PROVISIONED'
        }
    )
    Logger.log.info('Kinesis Stream %s created!' % (stream_name))
except Exception as e:
    pass

consumer = KinesisStreamConsumer(stream_name, profile_name)
producer = KinesisStreamProducer(stream_name, profile_name)

# TODO FIX ERROR
#Rate exceeded for shard shardId-000000000000 

target='jcooloj@500010349783-NB'
target='ALL'

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['git','pull']
}
producer.produce(data,'command')


data = {
    "sender" : "MASTER",
    "target" : "jcooloj@500010349783-NB",
    "job" : "command",
    "command" : ['pip','install','-r','requirements.txt']
}
producer.produce(data,'command')


data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "restart",
}
producer.produce(data,'command')


target = 'jcooloj@TRADEBOT01-PC'
repo = 'MarketData-CSIData'
data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['git','clone','https://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@github.com/jcarlitooliveira/repo',\
        '..\\'+repo]
}
producer.produce(data,'command')


data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "ping",    
}
producer.produce(data,'command')


data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['set']
}
producer.produce(data,'command')


data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['shutdown','/f','/r']
}
producer.produce(data,'command')


data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['RD','/S','/Q','..\\SharedData'],
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['nvidia-smi','--query-gpu=gpu_name,gpu_bus_id,vbios_version','--format=csv'],
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
    "job" : "command",
    "command" : ['tasklist']
}
producer.produce(data,'command')

target = 'ALL'
data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['ping','8.8.8.8','-n','1']
}
producer.produce(data,'command')


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




response = client.delete_stream(
    StreamName=stream_name
)


