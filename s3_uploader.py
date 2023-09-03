import boto3
from aws_config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, BUCKET_NAME
from logging_config import LOGGING_FORMAT, LOGGING_DATE_FORMAT, LOGGING_LEVEL, LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=LOGGING_LEVEL, format=LOGGING_FORMAT, datefmt=LOGGING_DATE_FORMAT)

class S3Uploader:
  def __init__(self):
    self.s3 = boto3.client(
      's3',
      aws_access_key_id=AWS_ACCESS_KEY_ID,
      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
      region_name=AWS_REGION
    )

  def upload_file(self, file_path):
      file_name = file_path.split('/')[-1]
      self.s3.upload_file(file_path, BUCKET_NAME, file_name)
      logging.info(f"Uploaded {file_name} to {BUCKET_NAME}")
