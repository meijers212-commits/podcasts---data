import os
from pathlib import Path
from datetime import datetime


class MetadataExtractor:
    def __init__(self):
        self.folder_path = path = os.path.join(".", "podcasts")

    def get_size_in_MB(self, size_in_byts):

        size_in_KB = size_in_byts / 1024

        size_in_MB = size_in_KB / 1024

        return size_in_MB

    def get_metadata(self):
        folder_path = os.path.join(".", "podcasts")

        metadata = {}

        for file in os.listdir(path=folder_path):

            file_path = os.path.join(folder_path, file)

            metadata[file] = {
                "file_size" : os.path.getsize(file_path),
                "file_size_in_MB": self.get_size_in_MB(os.path.getsize(file_path)),
                "create_time": str(datetime.fromtimestamp(os.path.getctime(file_path))),
            }

        return metadata



