import os 

class IngestionConfig:
    
    def __init__(self):
        
        self.BOOTSTRAP_SERVERS = os.getenv('BOOTSTRAP_SERVERS', 'localhost:9092')

       