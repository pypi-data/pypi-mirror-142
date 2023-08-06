import boto3
import os
from botocore.config import Config
import json

class AWSClient:
  instance = None

  # Singleton to instantiate client only one time between lambdas in warm start
  def __new__(cls, *args, **kwargs):
      if not isinstance(cls.instance, cls):
          cls.instance = object.__new__(cls)
      return cls.instance

  def __init__(self):
    self.s3 = boto3.client("s3")
    self.kinesis = boto3.client("kinesis", config=Config(region_name = os.environ['AWS_REGION']))
    
  # Define new AWS Client if not already instantiated
  def getAWSClient(self):
    return self

  # Kinesis
  def kinesisPutRecord(self, streamName, rawData, partitionKey):
    response = self.kinesis.put_record(
      StreamName=streamName,
      Data=json.dumps(rawData),
      PartitionKey=partitionKey,
    )
    return response
