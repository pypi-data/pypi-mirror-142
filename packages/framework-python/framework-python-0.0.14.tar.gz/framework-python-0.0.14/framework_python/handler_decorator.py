import os
import sentry_sdk
import logging
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
from .aws_client import AWSClient

# Initialize sentry, logger and AWS X-Ray
def handler_decorator(handler):
  def wrapper(*args, **kwargs):
    
    # Logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # AWS X-Ray patch all traces 
    patch_all()

    # Initialize AWS Client
    AWSClient()

    # Sentry
    sentry_sdk.init(
      dsn = os.environ['SENTRY_DSN'] if "SENTRY_DSN" in os.environ else "",
      traces_sample_rate=1.0
    )
    try:
      return handler(*args, **kwargs)
    except Exception as err:
      sentry_sdk.capture_exception(err)
      client = sentry_sdk.Hub.current.client
      if client is not None:
        client.flush(timeout=1)
      raise Exception(str(err))

  return wrapper