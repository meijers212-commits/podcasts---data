import os
import sys
from ingestion_orchestrator import logger

class IngestionConfig:

    def __init__(self):

        self.BOOTSTRAP_SERVERS = os.getenv('BOOTSTRAP_SERVERS')
        self.PUBLISHER_TOPIC = os.getenv('PUBLISHER_TOPIC', 'wav-metadata')
        self.FOLDER_PATH = os.getenv('FOLDER_PATH')

        self.validate()

    def validate(self):

        required_vars = {
            "BOOTSTRAP_SERVERS": self.BOOTSTRAP_SERVERS,
            "PUBLISHER_TOPIC": self.PUBLISHER_TOPIC,
            "FOLDER_PATH": self.FOLDER_PATH
        }

        missing = []

        for name, value in required_vars.items():
            if value is None or value.strip() == "":
                missing.append(name)

        if missing:
            logger.error(f"Necessary environment variables are missing to run the service: {missing}")
            sys.exit(1)

        if not os.path.exists(self.FOLDER_PATH):
            logger.error(f"Error: folder: {self.FOLDER_PATH}, does not exist")
            sys.exit(1)

        logger.info("All variables have been loaded and are ready to use.")

config = IngestionConfig()