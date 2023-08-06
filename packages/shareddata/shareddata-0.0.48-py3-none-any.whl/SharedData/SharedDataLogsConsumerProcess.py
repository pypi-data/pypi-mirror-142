from SharedData.Logger import Logger
from SharedData.SharedDataAWSKinesis import KinesisLogStreamConsumer

logger = Logger(__file__)
Logger.log.info('Starting SharedDataLogsConsumer process')
consumer = KinesisLogStreamConsumer()
dflogs = consumer.readLogs()
stream = consumer.connect()
Logger.log.info('Starting SharedDataLogsConsumer process STARTED!')
consumer.loop()