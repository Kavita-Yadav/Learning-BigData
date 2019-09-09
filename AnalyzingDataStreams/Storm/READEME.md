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

