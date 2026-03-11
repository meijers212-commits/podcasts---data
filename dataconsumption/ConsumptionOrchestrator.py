from consumptionconfig import ConsumptionConfig
from consumptionconsumer import ConsumptionConsumer
import json
from mongoclient import MongoConnection
from elasticsearchclient import ElasticsearchClient
from logger import logger



def run():
    
    config = ConsumptionConfig()

    consum = ConsumptionConsumer(config=config)

    consumer = consum.get_consumer()

    topics = config.CONSUMER_TOPIC

    mongo = MongoConnection(config)

    es = ElasticsearchClient(config)

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
                
                data["id"] = str(hash(data["file_name"]))

                mongo.insert_doc(data)
                
                if '_id' in data:
                    del data['_id']

                es.index_record(data)
                
                logger.info(f"doc 📄: {data.get('file_name', '')} - inserted to mongodb")

            except Exception as e:
                logger.error(f"Error occurred {e}")
                raise e

            

    finally:
        consumer.unsubscribe()
        consumer.close()


run()
