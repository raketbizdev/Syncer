import time
import logging
from file_watcher import Watcher
from s3_uploader import S3Uploader
from logging_config import LOGGING_FORMAT, LOGGING_DATE_FORMAT, LOGGING_LEVEL, LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=LOGGING_LEVEL, format=LOGGING_FORMAT, datefmt=LOGGING_DATE_FORMAT)

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