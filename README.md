# Syncer

## Overview

Syncer is a Python script that monitors a specified local directory for new or updated files and automatically uploads them to an Amazon S3 bucket.

## Prerequisites

- Python 3.x
- Watchdog
- Boto3

## Installation

1. Clone the repository or download the source code.

   ```
   git clone git@github.com:raketbizdev/Syncer.git
   ```

2. Navigate into the project directory.

   ```
   cd Syncer
   ```

3. Install the required packages.

   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Open `aws_config.py` and fill in your AWS Access Key, Secret Key, and other configurations.

   ```
   AWS_ACCESS_KEY_ID = 'YOUR_ACCESS_KEY_ID'
   AWS_SECRET_ACCESS_KEY = 'YOUR_SECRET_ACCESS_KEY'
   AWS_REGION = 'YOUR_REGION'
   BUCKET_NAME = 'company-x'
   DIRECTORY_TO_WATCH = 'company-file'
   ```

2. Set up logging configurations in `logging_config.py` if needed. By default, logs are written to `s3syncer.log`.

## Usage

Run the script by executing:

```
python main.py
```

This will start monitoring the directory specified in `aws_config.py`. Any new or updated files will automatically be uploaded to the configured S3 bucket.

## Logging

Check `s3syncer.log` for logs. The log level and format can be configured in `logging_config.py`.

## License

This project is licensed under the MIT License. See the LICENSE.md file for details.
