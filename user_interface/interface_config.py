import os
import sys

class UserConfig:

    def __init__(self, logger):

        self.logger = logger

        self.ES_URI = os.getenv("ES_URI", "http://elasticserch:9200")
        self.ES_INDEX = os.getenv("ES_INDEX", "podcasts")

        self.ADMIN_USER_NAME = os.getenv("ADMIN_USER_NAME", "admain")
        self.ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admain")

        self.validate()

    def validate(self):

        required_vars = {
            "ES_URI": self.ES_URI,
            "ES_INDEX": self.ES_INDEX,
            "ADMIN_USER_NAME": self.ADMIN_USER_NAME,
            "ADMIN_PASSWORD": self.ADMIN_PASSWORD
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

        self.logger.info("All variables have been loaded and are ready to use.")



