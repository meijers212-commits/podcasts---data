from IngestionConfig import IngestionConfig
from metadataextractor import MetadataExtractor
from Ingestionpublisher import KafkaPublisher
from logger import Logger

config = IngestionConfig()

md_extractor = MetadataExtractor(config)

publisher = KafkaPublisher(config)

logger = Logger.get_logger()

def run():

    try:
        
        logger.info('starting to send data to kafka..')

        metadata = md_extractor.get_metadata()

        for wav in metadata:

            publisher.publish(wav)

        logger.info('data sent to kafka sexssfuly !')

    except KeyboardInterrupt:
        
        logger.info("stopping ...")

    finally:

        publisher.flush()


run()
