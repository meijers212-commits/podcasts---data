from IngestionConfig import IngestionConfig
from metadataextractor import MetadataExtractor
from kafkapublisher import KafkaPublisher

config = IngestionConfig()

md_extractor = MetadataExtractor(config)

publisher = KafkaPublisher(config)


def run():

    try:

        metadata = md_extractor.get_metadata()

        for wav in metadata:

            publisher.poblish(wav)

    except KeyboardInterrupt:
        print("stopping ...")

    finally:

        publisher.flush()


run()
