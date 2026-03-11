from IngestionConfig import IngestionConfig
from metadataerxtractor import MetadataExtractor
from Ingestionpublisher import KafkaPublisher
from logger import logger
from stt import speech_to_text
import os 


def run():
    
    config = IngestionConfig()

    md_extractor = MetadataExtractor(config)

    publisher = KafkaPublisher(config)

    folder_path = config.FOLDER_PATH

    try:

        for file in os.listdir(path=folder_path):

            try:
                
                file_path = os.path.join(folder_path, file)

                wav = md_extractor.get_metadata(file, file_path)

                wav["file_text"] = speech_to_text(file_path)

                logger.info(f'sending data: {wav.get("file_name","")} to kafka..')

                publisher.publish(wav)

                logger.info('data sent to kafka sexssfuly !')

            except Exception as e:
                logger.error(f'Error occurred while andeling file {file_path} , ERROR: {e}')

    except KeyboardInterrupt:
        
        logger.info("stopping ...")

    finally:

        publisher.flush()


run()
