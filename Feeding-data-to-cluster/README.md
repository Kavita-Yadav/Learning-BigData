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
           *Connectors*        DB ------> |    Kafka Cluster      |<-----------> App      *Stream Processors*
                            ,------------- _______________________
                           |                    /    |    \
                          \|/                  /     |      \                    
                          DB                 \|/    \|/     \|/
                                             App    App     App
                          
                                                  *Consumers*
                          
                          
                          
