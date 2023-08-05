import boto3

class AWSClient:
  instance = None

  # Singleton to instantiate client only one time between lambdas in warm start
  def __new__(cls, *args, **kwargs):
      if not isinstance(cls.instance, cls):
          cls.instance = object.__new__(cls)
      return cls.instance

  def __init__(self):
    self.s3 = boto3.client("s3")
    
  # Define new AWS Client if not already instantiated
  def getAWSClient(self):
    return self
