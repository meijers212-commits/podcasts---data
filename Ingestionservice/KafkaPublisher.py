from confluent_kafka import Producer
import socket


class KafkaPublisher:

    def __init__(self, config):

        self.config = config

        self.conf = {
            "bootstrap.servers": self.config.BOOTSTRAP_SERVERS,
            "client.id": "Ingestionservice",
        }

        self.producer = Producer(self.conf)

    def acked(self,err, msg):
        if err is not None:
            print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            print("Message produced: %s" % (str(msg)))

    def poblish(self, plyload):
            
            self.producer.produce(self.config.topic, value=plyload, callback=self.acked())
            
            self.producer.poll(1)
