from kafka import KafkaAdminClient, TopicPartition
from kafka.admin import NewTopic



admin_client = KafkaAdminClient(bootstrap_servers=['ip_broker0:9093', 'ip_broker1:9094', 'ip_broker2:9095'],
    client_id='test'
    )

topic_list = []
topic_list.append(NewTopic(name="tes3", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)