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
    self.kinesis_firehose = boto3.client("firehose", config=Config(region_name = os.environ['AWS_REGION']))
    
  # Define new AWS Client if not already instantiated
  def getAWSClient(self):
    return self

  # Kinesis
  def kinesisFirehosePutRecord(self, delivery_stream_name, raw_data):
    response = self.kinesis_firehose.put_record(
      DeliveryStreamName=delivery_stream_name,
      Record = {
        'Data': json.dumps(raw_data),
      }
    )
    return response
