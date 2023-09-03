from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from aws_config import DIRECTORY_TO_WATCH
from logging_config import LOGGING_FORMAT, LOGGING_DATE_FORMAT, LOGGING_LEVEL, LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=LOGGING_LEVEL, format=LOGGING_FORMAT, datefmt=LOGGING_DATE_FORMAT)

class Handler(FileSystemEventHandler):

  def __init__(self, s3_uploader):
    self.s3_uploader = s3_uploader

  def process(self, event):
    if event.is_directory:
      return
    elif event.event_type == 'created' or event.event_type == 'modified':
      self.s3_uploader.upload_file(event.src_path)
      logging.info(f"Processed file {event.src_path}")

  def on_modified(self, event):
    self.process(event)

  def on_created(self, event):
    self.process(event)

class Watcher:

  def __init__(self, s3_uploader):
    self.observer = Observer()
    self.s3_uploader = s3_uploader

  def run(self):
    event_handler = Handler(self.s3_uploader)
    self.observer.schedule(event_handler, DIRECTORY_TO_WATCH, recursive=True)
    self.observer.start()
    print(f"Watching directory: {DIRECTORY_TO_WATCH}")
