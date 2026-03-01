import os 

class IngestionConfig:

    def __init__(self):
        
        self.BOOTSTRAP_SERVERS = os.getenv('BOOTSTRAP_SERVERS', 'localhost:9092')
        self.PUBLISHER_TOPIC = os.getenv('PUBLISHER_TOPIC', 'wav-metadata')
        self.FOLDER_PATH = os.getenv('FOLDER_PATH' , '.\podcasts')


        