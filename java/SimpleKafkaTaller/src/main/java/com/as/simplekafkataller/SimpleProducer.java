
package com.as.simplekafkataller;

import java.util.Properties;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;

/**
 *
 * @author Asullom
 */
public class SimpleProducer {
    public static void main(String[] args) throws Exception{
      
      // Check arguments length value
      //if(args.length == 0){
      //   System.out.println("Enter topic name");
      //   return;
      //}
      
      //Assign topicName to string variable
      String topicName = "streams-plaintext-input";//args[0].toString();
      
      // create instance for properties to access producer configs   
      Properties props = new Properties();
      
      //Assign localhost id
      props.put("bootstrap.servers", "localhost:9092");
      
      
      props.put("key.serializer", 
         "org.apache.kafka.common.serialization.StringSerializer");
         
      props.put("value.serializer", 
         "org.apache.kafka.common.serialization.StringSerializer");
      
      Producer<String, String> producer = new KafkaProducer <String, String>(props);
            
      for(int i = 0; i < 5; i++)
         producer.send(new ProducerRecord<String, String>(topicName, 
            Integer.toString(i), Integer.toString(i)));
               System.out.println("xMessage sent successfully");
               producer.close();
   }
}
