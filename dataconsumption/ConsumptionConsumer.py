from confluent_kafka import Consumer


class ConsumptionConsumer:
    def __init__(self, config):

        self.config = self.config
        self.consumer = Consumer(self.config.conf)
        self.topic = self.config.CONSUMER_TOPIC

    
    running = True

    async def basic_consume_loop(self):
         
        topics = self.topic
        consumer = self.consumer
        

        try:
            consumer.subscribe(topics)

           
            while True:
                msg = await consumer.poll(timeout=1.0)
                if msg is not None and not msg.error():
                    print(f'Consumed: {msg.value()}')
                    await consumer.store_offsets(message=msg)

        finally:
            await consumer.unsubscribe()
            await consumer.close()

    def shutdown():
        running = False

