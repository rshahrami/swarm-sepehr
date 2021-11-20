from kafka import KafkaProducer
import json

message_body='mozs'
key_kaf='reza4'

producer = KafkaProducer(bootstrap_servers=['ip_broker0:9093', 'ip_broker1:9094', 'ip_broker2:9095'],
                        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                        key_serializer=str.encode,
                        client_id='test',
                        )

producer.send('test', key=key_kaf, value=message_body)
producer.flush()