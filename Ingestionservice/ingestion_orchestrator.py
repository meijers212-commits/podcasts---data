from shared.logging.logger import Logger
from ingestion_config import IngestionConfig
from metadata_erxtractor import MetadataExtractor
from stt import speech_to_text
import os
from shared.kafka.kafka_producer import KafkaPublisher
from grid_fs import save_file_mongodb
from shared.mongo.mongo_client import MongoConnection

logger = Logger.get_logger(name="ingestion_service")


def run():

    config = IngestionConfig(logger=logger)

    mongo = MongoConnection(
        logger=logger, mongo_uri=config.MONGO_URI, db_name=config.MONGO_DB_NAME
    )

    md_extractor = MetadataExtractor(config)

    publisher = KafkaPublisher(
        logger=logger,
        bootstrap_service=config.BOOTSTRAP_SERVERS,
        publisher_topic=config.PUBLISHER_TOPIC,
        client_id="Ingestionservice",
    )

    folder_path = config.FOLDER_PATH

    try:

        for file in os.listdir(path=folder_path):

            try:

                file_path = os.path.join(folder_path, file)

                save_file_mongodb(
                    logger=logger,
                    mongo_db=mongo.client[config.MONGO_DB_NAME],
                    file_name=str(file),
                    file_path=file_path,
                )

                wav = md_extractor.get_metadata(file, file_path)

                wav["file_text"] = speech_to_text(file_path, logger)

                logger.info(f'sending data: {wav.get("file_name","")} to kafka..')

                publisher.publish(wav)

                logger.info("data sent to kafka sexssfuly !")

            except Exception as e:
                logger.error(
                    f"Error occurred while andeling file {file_path} , ERROR: {e}"
                )

    except KeyboardInterrupt:

        logger.info("stopping ...")

    finally:

        publisher.flush()


run()
