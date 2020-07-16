# Taller #5: Comunicación asíncrona de microservicios y big data con apache kafka. 
Este taller está dirigido a programadores donde se usa Apache Kafka para desarrollar dos casos de uso: La comunicación asíncrona de microservicios entre aplicaciones productores y consumidores escritos en diferentes plataforma de software como Java, JavaScript y Python. Y el caso de uso kafka streaming para aplicaciones de big data.
Requisitos: Haber desarrollado aplicaciones en cualquier lenguaje de programación

Por Angel Sullon 

## Caso de uso 1: Comunicación asíncrona entre productores y consumidores

### Para ejecutar los comandos deberás estar en la carpeta raiz de kafka
	Por ejemplo Ejemplo
	D:...\>cd kafka_2.12-2.5.0
	D:...\>kafka_2.12-2.5.0>

### Comando para iniciar el servidor kafka
	Start Zookeeper
	bin\windows\zookeeper-server-start.bat config\zookeeper.properties

	Start Kafka Broker
	bin\windows\kafka-server-start.bat config\server.properties


### Comando para crear e iniciar el topic
	Create topic
	bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic streams-plaintext-input

	no exec>bin\windows\kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic streams-plaintext-input2

	List topic	
	bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
	no exec>bin\windows\kafka-topics.bat --list --zookeeper localhost:2181

### Comando para testear el topic por command line
	Start Producer
	bin\windows\kafka-console-producer.bat --bootstrap-server localhost:9092 --topic streams-plaintext-input

	no exec>bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic streams-plaintext-input

	Start Consumer
	bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic streams-plaintext-input --from-beginning

### Code JavaScript (JS)
	
	D:...\J201-tallerkafka\js_consumer1>npm install
	>node index.js

	//Si desea crear de cero	
	D:...\J201-tallerkafka\js_consumer1>npm init
	>npm i --s kafka-node
	>goto > index.js
	>node index.js




## Caso de uso 2: Kafka Streams (sobre el caso de uso 1)

### Crear un nuevo topic
	bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic streams-wordcount-output --config cleanup.policy=compact

	//no exec>bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic streams-plaintext-input

	bin\windows\kafka-topics.bat --bootstrap-server localhost:9092 --describe

### Inicie un nuevo Consumer
	bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic streams-wordcount-output --from-beginning --formatter kafka.tools.DefaultMessageFormatter --property print.key=true --property print.value=true --property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer --property value.deserializer=org.apache.kafka.common.serialization.LongDeserializer

	//no exec>bin\windows\kafka-console-producer.bat --bootstrap-server localhost:9092 --topic streams-plaintext-input

### Inicie un el programa contado de palabra WordCountDemo de java
	////run WordCountDemo class
	////bin\windows\kafka-run-class.bat org.apache.kafka.streams.examples.wordcount.WordCountDemo
	////bin\windows\kafka-run-class.bat com.as.kafka.WordCountDemo

