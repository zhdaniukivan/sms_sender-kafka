from kafka import KafkaConsumer
import json

high_priority_consumer = KafkaConsumer(
    'high_priority',
    bootstrap_server='localhost:9002',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='high_priority_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

low_priority_consumer = KafkaConsumer(
    'low_priority',
    bootstrap_server='localhost:9002',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='low_priority_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def handle_high_priority():
    for message in high_priority_consumer:
        user = message.values
        print(f'High priority message received: {user}')

def handle_low_priority():
    for message in low_priority_consumer:
        user = message.value
        print(f'Low priority message received: {user}')
