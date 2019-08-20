###################
#### Cassandra ####
###################

#### Overview

- NoSQL with a twist
- Unlike HBase there is no master node at all, every node runs exactly the same software and performs the same functions.
- Data model is similar to BigTable/HBase.
- It is non relational, but has a limited CQL query language as its interface.

#### Where cassandra Fits in CAP trade offs ?

                            Availability
                                 / \
                      MySQL    /     \  Cassandra
                             /         \
                           /             \
                   Consistency ------- Partition-Tolerance
                      
                        Apache          mango
                        HBASE
                        
#### Cassandra Architecture:
      
                      -----node-----
                     |              |
                   node            node
                     |              |
                      -----node-----
                      
#### Cassandra and cluster:
  - cassandra is great for fast access to rows of info.
  - get the best of both worlds-replicate cassandra to another ring that is used to analytics and spark integration.
  
                      -----node-----                -----node-----
                     |              |              |              |
                   node            node   <--->   node           node 
                     |              |              |              |
                      -----node-----                -----node-----
