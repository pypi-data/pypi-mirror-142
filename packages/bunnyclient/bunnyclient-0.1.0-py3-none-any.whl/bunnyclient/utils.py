from pika import exchange_type
from config.connection import ConnectionFactory


def create_queue_and_exchange(
    queue_name,
    exchange_name,
    routing_key,
    queue_type="classic",
    queue_size=10,
    create_dl_objects=False,
):
    """
        example of the creation exchange and queues with dead-letter:

        {
            "queue_name": "product_creation_queue",
            "exchange_name": "product_topic",
            "routing_key": "create",
            "queue_type": "quorum",
            "create_dl_objects: True
        }

    Args:
        queue_name (str): queue name
        exchange_name (str): exchange name
        routing_key (str): the routing key pass
        queue_type (str, optional): type of queue. Defaults to "classic".
        queue_size (int, optional): size of queue. Defaults to 10.
        create_dl_objects (bool, optional): if True create a dead letter exchange and queue. Defaults to False.
    """
    connection = ConnectionFactory.get_connection()

    channel = connection.channel()

    arguments = {
        "x-queue-type": queue_type,
        "x-max-length": queue_size,
    }

    if create_dl_objects:
        dead_letter_exchange = f"dlx_{exchange_name}"
        dead_letter_queue = f"{queue_name}_dlq"

        channel.exchange_declare(
            exchange=dead_letter_exchange,
            exchange_type=exchange_type.ExchangeType.fanout,
        )

        channel.queue_declare(
            queue=dead_letter_queue, durable=True, arguments={"x-queue-mode": "lazy"}
        )
        channel.queue_bind(queue=dead_letter_queue, exchange=dead_letter_exchange)

        arguments["x-dead-letter-exchange"] = dead_letter_exchange

    channel.exchange_declare(
        exchange=exchange_name, exchange_type=exchange_type.ExchangeType.topic
    )

    channel.queue_declare(queue=queue_name, durable=True, arguments=arguments)
    channel.queue_bind(
        queue=queue_name, exchange=exchange_name, routing_key=routing_key
    )

    channel.close()
    connection.close()


schema = {
    "queue_name": "product_creation_queue",
    "exchange_name": "product_topic",
    "routing_key": "create",
    "queue_type": "quorum",
    "create_dl_objects": True,
}

create_queue_and_exchange(**schema)
