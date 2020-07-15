# Taller de Kafka 
Comunicación asíncrona de microservicios y big data con apache kafka. 
Por Angel Sullon 


## Comando para iniciar el servidor kafka

	Start Zookeeper
	>bin\windows\zookeeper-server-start.bat config\zookeeper.properties

	Start Kafka Broker
	>bin\windows\kafka-server-start.bat config/server.properties


## Comando para crear e iniciar el topic
	Create topic
	1>bin\windows\kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

	2>bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test2

	List topic
	1>bin\windows\kafka-topics.bat --list --zookeeper localhost:2181
	2>bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092

## Comando para testear el topic por command line
	Start Producer
	>bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic test

	Start Consumer
	>bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test --from-beginning

## Code JavaScript (JS)

	D:...\J201-tallerkafka\js_consumer1>npm init
	>npm i --s kafka-node
	>goto > index.js
	>node index.js
