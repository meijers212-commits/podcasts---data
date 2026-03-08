from analizer_config import AnalizerConfig
from analizer_consumer import AnalizerConsumer
from analizer_publiser import AnalizerPublisher
from text_analysis import Analizer
from logger import logger
import json

config = AnalizerConfig()

analizer_consumer = AnalizerConsumer(config)

publisher = AnalizerPublisher(config)

consumer = AnalizerConsumer.get_consumer()

analizer = Analizer()

try:

    while True:

        msg = consumer.poll(timeout=1.0)

        if msg is None:
            continue

        if msg.error():
            logger.error(f"Kafka Error: {msg.error()}")
            continue

        try:
            data = json.loads(msg.value().decode("utf-8"))
            logger.info(f"Consumed wav: {data.get('file_name', '')}")

            logger.info(f"processing wav: {data.get('file_name', '')}")
            
            object = analizer.bds_percent(data)
            
            publisher.publish(object)
               
            logger.info(f"doc 📄: {data.get('file_name', '')} - sent to kafka")

        except Exception as e:
            logger.error(f"Error occurred {e}")
            continue

finally:
    consumer.unsubscribe()
    consumer.close()
    publisher.flush()
    