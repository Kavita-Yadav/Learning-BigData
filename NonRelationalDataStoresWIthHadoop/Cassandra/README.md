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
      
                      ------node------
                     |                |
                   node  Cassandra  node
                     |                |
                      ------node------
                      
#### Cassandra and cluster:
  - cassandra is great for fast access to rows of info.
  - get the best of both worlds-replicate cassandra to another ring that is used to analytics and spark integration.
  
                      -----node-----                -----node-----
                     |              |              |              |
                   node     C1     node  <--->   node      C2    node <----> hadoop
                     |              |              |              |
                      -----node-----                -----node-----

#### CQL: 
  - Cassandra's API is CQL, which makes it easy to look like existing database drivers  to applications.
  - CQL is like SQL, but with some big limitations!
      - NO JOINS
        - Your data must be de-normalized
        - So, it's still non-relational
      - All queries must be on some primary key.
        - Secondary indices are supported, but primary key is always give best performance.
   - CQLSH can be used on the command line to create tables, etc.
   - All tables must be in a keyspace-keyspaces are like databases.
   
 #### Cassandra and Spark:
          Cassandra + Spark = best performer
       - DataStax offers a Spark-Cassandra connector.
       - Allows you to read and write Cassandra tables as DataFrames.
       - Is smart about passing queries on those DtaaFrames down to the appropriate level.
       - Use cases:
            - Use Spark for analytics on data stored in Cassandra.
            - Use Spark to transform data and store it into Cassandra for transactional use.
