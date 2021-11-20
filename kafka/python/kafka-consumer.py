from kafka import KafkaConsumer, TopicPartition

import json


consumer =  KafkaConsumer(
    bootstrap_servers=['ip_broker0:9093', 'ip_broker1:9094', 'ip_broker2:9095'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    # group_id='hassbtyan',
    )

# get_key = []
topic_name='test'
tp = TopicPartition(topic_name, 1)

# get_num_of_partitions=len(str(consumer.partitions_for_topic(topic_name)).split(', '))

# get_describe_topic=str(consumer.end_offsets([tp]))
# res = re.findall(r'\w+', get_describe_topic)
# get_topic_name = res[2]
# get_partition = res[4]
# get_end_offset = res[5]


# print("number of partitions is: " + str(get_num_of_partitions))
# print("topic name is: " + str(get_topic_name))
# print("partition is: " + str(get_partition))
# print("end of offset is: " + str(get_end_offset))

# consumer.assign([tp])
# consumer.poll()

# for msg in consumer:
    # print(msg.topic, msg.partition , msg.offset, msg.key, msg.value, msg.timestamp)

print(consumer.beginning_offsets([tp]))
print(consumer.end_offsets([tp]))

for msg in consumer:
  message_bytes_value = msg.value
  message_string_value = json.loads(message_bytes_value.decode())
#   print(message_string_value)
  count=count+1
  print(msg.topic, msg.partition, msg.offset, msg.key, message_string_value, count)



