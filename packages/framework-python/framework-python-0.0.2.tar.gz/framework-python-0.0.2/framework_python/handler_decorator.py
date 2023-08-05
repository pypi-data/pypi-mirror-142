import os
import json
import sentry_sdk
import logging
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all


# Initialize sentry, logger and AWS X-Ray
def handler_decorator(handler):
  def wrapper(*args):
    
    # Logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # AWS X-Ray patch all traces 
    patch_all()

    # Sentry
    sentry_sdk.init(
      dsn = os.environ['SENTRY_DSN'] if "SENTRY_DSN" in os.environ else "",
      environment=os.environ['ENVIRONMENT'] if "ENVIRONMENT" in os.environ else "",
      sample_rate=1.0
    )
    try:
      return handler(*args)
    except Exception as err:
      sentry_sdk.capture_exception(err)
      return {
        "statusCode": 500,
        "body": json.dumps({"error": err }),
      }

  return wrapper