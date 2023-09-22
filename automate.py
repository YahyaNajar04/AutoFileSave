import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

download_directory = "C:/Users/mynaj/Downloads"

extension_to_directory = {
    '.pdf': 'C:/Users/mynaj/Desktop/Year 2 sem 2',
    '.jpeg': 'C:/Users/mynaj/Pictures/downloaded images'
}

keyword_to_directory = {
    'SAT': 'C:/Users/mynaj/Desktop/Year 2 sem 2/Software Architecture and Testing',
    'Software Architecture and Testing': 'C:/Users/mynaj/Desktop/Year 2 sem 2/Software Architecture and Testing'
}


class DownloadsHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            src_file = event.src_path
            filename = os.path.basename(src_file)
            file_extension = os.path.splitext(filename)[1]

            if file_extension in extension_to_directory:
                target_directory = extension_to_directory[file_extension]
                shutil.move(src_file, os.path.join(target_directory, filename))

            for keyword, target_dir in keyword_to_directory.items():
                if keyword.lower() in filename.lower():
                    shutil.move(src_file, os.path.join(target_dir, filename))


if __name__ == "__main__":
    event_handler = DownloadsHandler()
    observer = Observer()
    observer.schedule(event_handler, path=download_directory, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
