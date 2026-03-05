import os 

class IngestionConfig:

    def __init__(self):
        
        self.BOOTSTRAP_SERVERS = os.getenv('BOOTSTRAP_SERVERS', 'kafka:29092')
        self.PUBLISHER_TOPIC = os.getenv('PUBLISHER_TOPIC', 'wav-metadata')
        self.FOLDER_PATH = os.getenv('FOLDER_PATH' , '/app/podcasts')


        