import os
import sys



class IngestionConfig:

    def __init__(self, logger):

        self.logger = logger
        self.BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS")
        self.PUBLISHER_TOPIC = os.getenv("PUBLISHER_TOPIC")
        self.FOLDER_PATH = os.getenv("FOLDER_PATH")
        self.MONGO_URI = os.getenv("MONGO_URI")
        self.MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")



        self.validate()

    def validate(self):

        required_vars = {
            "BOOTSTRAP_SERVERS": self.BOOTSTRAP_SERVERS,
            "PUBLISHER_TOPIC": self.PUBLISHER_TOPIC,
            "FOLDER_PATH": self.FOLDER_PATH,
        }

        missing = []

        for name, value in required_vars.items():
            if value is None or value.strip() == "":
                missing.append(name)

        if missing:
            self.logger.error(
                f"Necessary environment variables are missing to run the service: {missing}"
            )
            sys.exit(1)

        if not os.path.exists(self.FOLDER_PATH):
            self.logger.error(f"Error: folder: {self.FOLDER_PATH}, does not exist")
            sys.exit(1)

        self.logger.info("All variables have been loaded and are ready to use.")


# def get_config():
#     config = IngestionConfig()
#     return config
