###############
#### Storm ####
###############

Real-time stream processing

#### What is Storm ?

- Another framework for processing continour streams of data on a cluster
     - Can run on top of YARN (like Spark)
- Works on individual events, not micro-batches (like Spark Streaming does)
     - If you need sub-second latency, Storm is for you
     
#### Storm terminology

- A stream consists of tuples that flow through...
- Spouts that are sources of stream data (Kafka, Twitter, etc.)
- Bolts that process stream data as it's received
    - Transform, aggregate, write to database / HDFS
- A toplogy is graph of spouts and bolts that process your stream

          ,-------->  Bolt -------> Bolt
         |                          /|\
      Spout-----------.              |
                     \|/             |
                 ,->  Bolt ----------'
                |     
      Spout-----'
        |        
        '--------->   Bolt

#### Storm Architecture
                                                                 
                                         Supervisor  
                                      
                         Zookeeper       Supervisor 
                         
         Nimbus          Zookeeper       Supervisor 
         
                         Zookeeper       Supervisor 
                         
                                         Supervisor 
                                      
#### Developing Storm applications

- Usually done with Java
     - Although bolts may be directed through scripts in other languages
- Storm Core
     - The loer-level API for Storm
     - "At-least-once" semantics
- Trident
     - Higher-levle API for Storm
     - "Exactly-level API for Storm
- Storm runs your applications "forever" once submitted- until you explicitly stop them

#### Storm vs Spark Streaming

- With spark's streaming can do things like integrate with MLLib for machine learning or integrate with GraphX and lot more.
- With spark you can develop something using python or scala, there are lot of example you can find regard it but in case of   storm, you need to be master in java. 
- Storm is best suitable for real time processing comparitive to spark streaming. Storm do real time processing sub-second     and an event by event basis whereas Spark streaming deals with micro batches which can be as little as one second, which     are not events.
- Core Storm offers "tumbling windows" in addition to "sliding windows".
- Kafka + Storm seems to be a pretty popular combination.

_Example: WordCount_

   - we'll run the WordCount topology example and examine it.
   
           _______________            __________            _____________
          |     Spout     |          |   Bolt   |          |     Bolt     |
          |    (random    | ------>  |  (split  | ------>  | (Keep count  |
          |    sentence   |          |  into    |          |   of words   |
          |    generator) |          |  words)  |          |   and emit   |
           _______________            __________           |   results)   |
                                                            ______________
 - Start Hadoop virtual box.
 - Login to Ambari as admin.
 - Start Storm Service.
 - Start Kafka Service.
 - Login to terminal as maria_dev
 - cd /usr/hdp/current
 - cd storm-client/
 - ls
 - cd contrib/storm-starter/src/jvm/org/apache/storm/
 - ls
 - vi WordCountTopology.java
 - storm jar /usr/hdp/current/storm-client/contrib/storm-starter/storm-starter-topologies-*.jar org.apache.storm.starter.WordCountTopology wordcount
 - Open storm UI 127.0.0.1:8744
 - In topology summary, click on 'wordcount' and see the details of what's going on there.
 - If you want to kill this process then you need to click on 'Kill' in Topology actions. At the end of completion you always need to kill the task otherwise this job will run forever.
 - Go back to terminal.
 - cd /usr/hdp/current/storm-client/logs
 - ls
 - cd worker-artifacts/
 - ls
 - cd wordcount-4-1487259618/
 - ls
 - cd 6700
 - ls -ltr
 - tail -f worker.log
 - exit
 - In web UI, Click on Kill in Topology actions -> OK
 - ACPI shutdown hadoop virtual box.
 
 
