# -*- coding: utf-8 -*-
"""
@author: Asullom
"""
# pip install kafka-python
from kafka import KafkaConsumer
from json import loads
import json
consumer = KafkaConsumer('streams-plaintext-input', 
                         bootstrap_servers=['localhost:9092'], 
                         api_version=(0, 10) 
                         #,consumer_timeout_ms=1000
                         #, value_deserializer=lambda m: json.loads(m.decode('utf8'))
                        )
print("pyconsumer")
for message in consumer:
    #print(message.value)
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))