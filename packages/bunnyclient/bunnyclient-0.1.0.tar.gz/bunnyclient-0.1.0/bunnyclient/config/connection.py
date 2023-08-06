import pika
from pika.adapters.blocking_connection import BlockingConnection
from config.environ import environment


class ConnectionFactory:
    @classmethod
    def get_connection(cls) -> BlockingConnection:
        credentials = pika.PlainCredentials(
            username=environment.RABBIT_USER, password=environment.RABBIT_PASSWORD
        )
        return pika.BlockingConnection(
            pika.ConnectionParameters(environment.RABBIT_HOST, credentials=credentials)
        )