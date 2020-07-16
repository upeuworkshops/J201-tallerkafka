const kafka = require('kafka-node');
const broker = new kafka.KafkaClient({kafkaHost: '127.0.0.1:9092'});

var consumer = new kafka.Consumer(broker, [ { topic: 'streams-plaintext-input' } ]);
console.log("JS Consumer1 iniciado");
consumer.on('message', function (message) {
        console.log(message);
    });
