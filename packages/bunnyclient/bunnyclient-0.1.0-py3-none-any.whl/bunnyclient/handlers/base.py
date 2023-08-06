import json
import abc
import threading
from typing import Optional
from config.connection import ConnectionFactory


class Publisher:

    def __init__(self, exchange_name: str) -> None:
        self.exchange_name = exchange_name
        self.connection = ConnectionFactory.get_connection()
        self.channel = self.connection.channel()

    def publish(self, data: dict, routing_key: Optional[str] = ''):
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=routing_key,
            body=json.dumps(data)
        )

        self.connection.close()

class Handler(abc.ABC):

    def __init__(self) -> None:
        self.connection = ConnectionFactory.get_connection()
        self.channel = self.connection.channel()
        self.publisher = Publisher(self.exchange_name)

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.get_messages, auto_ack=True)
        print('waiting messages...')
        thread = threading.Thread(target=self.channel.start_consuming)
        thread.start()

    def get_messages(self, ch, method, properties, body):
        messages = json.loads(body)
        self.handle(messages)

    @abc.abstractmethod
    def handle(self, messages):
        raise NotImplemented('this method must be implemented')