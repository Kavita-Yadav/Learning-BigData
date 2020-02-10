###############
#### Flink ####
###############

Another data stream framework!

#### What is Flink?

- Flink i german word for quick and nimble.
- Another stream processing engine- most similar to Storm.
- Can run on standalone cluster, or on top of YARN or Mesos.
- Highly scalable (1000's of nodes).
- Fault-tolerant
    - Can survive failure while still guaranteeing exactly-once processing.
    - Uses "state snapshots" to achieve this.
- Up & coming quickly

#### Flink vs Spark Streaming vs Storm

- Flink's faster than Storm.
- Flink offers "real streaming" like Storm (but if you're using Trident with Storm, you're using micro-batches).
- Flink has good Scala support, like Spark Streaming.
- Flink has an ecosystem of its own, like Spark.
- Flink can process data based on events times, not when data was recieved
    - Impressive windowing system
    - This plus real-time streaming and exactly-once semantics is important for financial applications.
- But it's the youngest of the technologies.

#### All three are converging it seems:

- Spark Streaming's "Structured Streaming" paves the way for real event-based streaming in Spark.
- Becomes more a question of what fits best in your existing environment.

#### Flink architecture:

     ___________________________                    __________________________________
    |     CEP      |            |                  |           |           |          |
    |  (Event      |    Table   |                  |  FlinkML  |   Gelly   |   Table  |
    |  processing) |            |                  |           |           |          |
     _____________________________________________________________________________________________
    |                DataStream API                |              DataSet API                     |
     _____________________________________________________________________________________________
    |                                     Flink Runtime                                           |
     _____________________________________________________________________________________________
    | Standalone cluster      |  YARN/Hadoop      |  AWS/ Google Cloud     |     Local            |
     _____________________________________________________________________________________________
    
    - It is run time engine like Spark.
    - It can run on standalone cluster.
    - It can process not only streaming data but also batch data.
    - It can handle bounded and unbounded data both.
    - It has two different API.
        DataStream API: can do event processing using CEP. Also can do table based processing where can issue sql like relational quieries on data.
        DataSet API: dealing with batch data.
    - FlinkML is like MLLib in spark.
    - Gelly is like spark graphx for graph processing.
    - Table is doing sql queries just like SparkQL.
    
    _Connectors:_
    - HDFS
    - Cassandra
    - Kafka
    - Others: Elasticsearch, NiFi, Redis, RabbitMQ
    
    _Example: WordCount_
    - Login to terminal as maria_dev.
    - wget https://apache.cs.utah.edu/flink/flink-1.2.0/flink-1.2.0-bin-hadoop27-scala_2.10.tgz
    - tar -xvf flink-1.2.0-bin-hadoop27-scala_2.10.tgz
    - ls
    - cd conf
    - ls
    - vi flink-conf.yaml
    
          jobmanager.web.port:8082
    - cd ..
    - ./bin/start-local.sh
    - Go to flink web UI 127.0.0.1:8082
    - Go back to terminal
    - nc -1 9000
    - open second terminal.
    - ./bin/flink run examples/streaming/SocketWindowWordCount.jar --port 9000.
    - Check the running job on web UI.
    - open 3rd terminal.
    - Type in 1st terminal: I am rock I am an island
    - In terminal 3rd; $ cd flink-1.2.0
    - cd log/
    - ls
    - ls -ltr
    - In 1st terminal; Ctrl + c exit.
    - exit
    - exit
    - ACPI shutdown.
    
        
    
    
