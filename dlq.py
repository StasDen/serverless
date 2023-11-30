from azure.servicebus import ServiceBusClient as servbuscl, ServiceBusSubQueue as servbusq
import os

CONNECTION_STR = os.environ["AZURE_SERVICEBUS_CONNECTION_STRING"]
QUEUE_NAME = os.environ["AZURE_QUEUE_NAME"]

client = servbuscl.from_connection_string(CONNECTION_STR)

# receiving dead letters
with client: 
    dlq_receiver = client.get_queue_receiver(queue_name=QUEUE_NAME, sub_queue=servbusq.DEAD_LETTER)
    with dlq_receiver as receiver:
        messages = receiver.receive_messages(max_message_count=10, max_wait_time=5)
        for msg in messages:
            receiver.complete_message(msg)  # removing from dlq
