# Constants for AWS and S3
AWS_ACCESS_KEY_ID = 'YOUR_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'YOUR_SECRET_ACCESS_KEY'
AWS_REGION = 'YOUR_REGION'
BUCKET_NAME = 'company-x'
DIRECTORY_TO_WATCH = 'company-file'

# Function to validate AWS constants
def validate_aws_config():
  errors = []
  
  if not AWS_ACCESS_KEY_ID or AWS_ACCESS_KEY_ID == 'YOUR_ACCESS_KEY_ID':
    errors.append("AWS_ACCESS_KEY_ID is missing or not configured.")
    
  if not AWS_SECRET_ACCESS_KEY or AWS_SECRET_ACCESS_KEY == 'YOUR_SECRET_ACCESS_KEY':
    errors.append("AWS_SECRET_ACCESS_KEY is missing or not configured.")
    
  if not AWS_REGION or AWS_REGION == 'YOUR_REGION':
    errors.append("AWS_REGION is missing or not configured.")
    
  if not BUCKET_NAME or BUCKET_NAME == 'company-x':
    errors.append("BUCKET_NAME is missing or not configured.")
    
  if not DIRECTORY_TO_WATCH or DIRECTORY_TO_WATCH == 'company-file':
    errors.append("DIRECTORY_TO_WATCH is missing or not configured.")
    
  if errors:
    raise Exception("\n".join(errors))

# Call the function to validate
validate_aws_config()
