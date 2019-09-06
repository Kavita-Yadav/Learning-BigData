###############
#### KAFKA ####
###############

Publish/subscribe Messaging wirh Kafka.

#### What is streaming ?
- SO far we've really just talked about processing historical, existing big data
    - Sitting on HDFS
    - Sitting in a database
- But how does new data get into your cluster? Especially if it's "Big data"?
    - New log entries from your web servers.
    - New sensor data from your IoT system.
    - New stock trades.
- Streaming lets you publish this data, in real time, to your cluster.
    - And you can even process it in real time as it comes in!
- Two problems to stream your data
    - How to get data from many different sources flowing into your cluster.
    - Processing it when it gets there.
    
#### Kafka
- Kafka is a general- purpose publish/subscribe messaging system.
- Kafka servers store all incoming messages from publishers for some period of time, and publishes them to a stream of data
  called a topic.
- Kafka consumers subscribe to one or more topics, and receive data as it's published.
- A stream/topic can have many different consumers, all with their own position in the stream maintained.
- It's not just for Hadoop. You can use this for any sort of application outside of hadoop as well.

#### Kafka architecture
    
                                                  *Producers*    
                                    
                                        App         App         App
                                         \           |           /
                                           \         |          /
                                           \|/      \|/       \|/
                                           _______________________
           *Connectors*   DB -----------> |    Kafka Cluster      |<-----------> App      *Stream Processors*
                            ,------------- _______________________
                           |                    /    |    \
                          \|/                  /     |      \                    
                          DB                 \|/    \|/     \|/
                                             App    App     App
                          
                                                  *Consumers*
 
 #### Setting up Kafka, and publishing some data
 - Login to Ambari as admin.
 - Start Kafka service.
 - Login to terminal as maria_dev.
 - cd /usr/hdp/current/kafka-broker/
 - cd bin
 - ./kafka-topics.sh --create --zookeeper sandbox.hortonworks.com:2181 --replication-factor 1 --partitions 1 --topic fred
 - ./kafka-topics.sh --list --zookeeper sandbox.hortonworks.com:2181
 - ./kafka-console-producer.sh --broker-list sandbox.hortonworks.com:6667 --topic fred
 - now open one more terminal and login as maria_dev.
 - cd /usr/hdp/current/kafka-broker/bin
 - ./kafka-console-consumer.sh --bootstrap-server sandbox.hortonworks.com:6667 --zookeeper localhost:2181 --topic fred --        from-beginning
 - Now try to type on one terminal and another terminal will automatically get the same message
 - Ctrl + C to cancel it.
 
 #### Publishing Web Logs with Kafka
 - cd conf
 - cp connect-standalone.properties ~/
 - cp connect-file-sink.properties ~/
 - cp connect-file-source.properties ~/
 - cd ~
 - vi connect-standalone.properties
    bootstrap.servers=sandbox.hortonworks.com:6667
 - vi connect-file-sink.properties
    file=/home/maria_dev/logout.txt
    topic=log-test
 - vi connect-file-source.properties
    file=/home/maria_dev/access_log_small.txt
    topic=log-test
 - wget http://media.sundog-soft.com/hadoop/access_log_small.txt
 - In another connected terminal; ./kafka-console-consumer.sh --bootstrap-server sandbox.hortonworks.com:6667 --topic log-      test --zookeeper localhost:2181
 - Again in first terminal; cd /usr/hdp/current/kafka-broker/bin
 - ./connect-standalone.sh ~/connect-standalone.properties ~/connect-file-source.properties ~/connect-file-sink.properties
 - Open one more terminal as maria_dev.
 - cd ~
 - less logout.txt
 - echo "This is a new line" >> access_log_small.txt
 - Check now another terminals it will generate this line on another two terminal as well.
 - exit from all 3 terminal.
 - Stop Kafka service at Ambari.
    
 
 
 
                          
