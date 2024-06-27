from kafka import KafkaProducer, KafkaConsumer
import json

produser = KafkaProducer(
    bootstrap_servers='lacalhost:9002',
    volue_serializer=lambda v: json.dumps(v).encode('utf-8')
)


def send_high_priority_message(user):
    produser.send('high_priority', {'username': user.username, 'email':user.email})
    produser.flush()


def send_low_priority_message(user):
    produser.send('low_priority', {'username':user.username, 'email':user.email})
    produser.flush()


