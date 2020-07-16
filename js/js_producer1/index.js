const kafka = require('kafka-node');
const broker = new kafka.KafkaClient({kafkaHost: '127.0.0.1:9092'});

var producer = new kafka.Producer(broker);

producer.on('ready', function () {
     setInterval(function() {
        producer.send( [ { topic: "streams-plaintext-input", messages: "Hola kafka."+new Date() } ], function (err,data) {        } );
        }, 5000); 
    });
console.log("JS Producer1 está enviando mensajes");