# -*- coding: utf-8 -*-
"""
https://kafka-python.readthedocs.io/en/master/usage.html#kafkaproducer
@author: Asullom
"""
# pip install kafka-python
from kafka import KafkaProducer
from kafka.errors import KafkaError
from json import loads
import json
# By default it take JSON serializer
producer = KafkaProducer(bootstrap_servers=['localhost:9092']
	,api_version=(0, 10)
	, value_serializer=lambda m: json.dumps(m, ensure_ascii=False).encode('utf8')
	)

# Topic name is streams-plaintext-input
future = producer.send('streams-plaintext-input', value={'key': 'valueó'})

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
    producer.close()
    print("DONE.")
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)

