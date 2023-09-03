import time
import logging
from file_watcher import Watcher
from s3_uploader import S3Uploader
from logging_config import LOGGING_FORMAT, LOGGING_DATE_FORMAT, LOGGING_LEVEL, LOG_FILE

# Initialize logging
logging.basicConfig(filename=LOG_FILE, level=LOGGING_LEVEL, format=LOGGING_FORMAT, datefmt=LOGGING_DATE_FORMAT)

# Validate AWS Configuration
try:
  import aws_config  # This will run validate_aws_config() and may raise an exception
except Exception as e:
  print(f"Error in AWS Configuration: {e}")
  logging.error(f"Error in AWS Configuration: {e}")
  exit(1)

if __name__ == '__main__':
  logging.info("Starting S3Syncer")
  s3_uploader = S3Uploader()
  watcher = Watcher(s3_uploader=s3_uploader)
  watcher.run()
  try:
    while True:
      time.sleep(5)
  except KeyboardInterrupt:
    logging.info("Observer Stopped")
