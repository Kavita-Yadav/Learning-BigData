## Why NoSQL ?

Random Access to Planet-Size Data

Scaling up MySQL etc. massive loads requires extreme measures:
- Denormalization
- Caching layers
- Master/slave setups
- Sharding
- Materialized views
- Removing stored procedures

Do you really need SQL?
- your high-transaction queries are probably preety simple once de-normalized.
- A simple get/put API may meet your needs.
- Looking up values for a given key is simple, fast, and scalable.
- You can do both.....

Sample Architecture:

        
                                Client & request
                                      router
                                 /     |     \
                                /      |       \
                           Shard 1   Shard 2  Shard N     
                              |        |         |
                           Shard 1   Shard 2  Shard N  
                           backup    backup   backup
                           
Use the right tool for the job:

- For analytic queries, Hive, Pig, Spark, etc. work great.
- Exporting data to MySQL is plenty fast for most applications too.
- But if you work at giant scale- export your data a non-relational database for fast and scalable serving of that data to
  web applications, etc.
  
Sample application architecture:

          Happy Customers
                |
             Internet
                |
            Web Servers
                |
               \|/          _______________
              MangoDB <-- |Spark Streaming| <--- Data source(s)
                          |_______________|
                          |     Hadoop    |
                          |   YARN/HDFS   |
                           _______________
  
