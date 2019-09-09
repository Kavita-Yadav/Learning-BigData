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
                                      
                                      
