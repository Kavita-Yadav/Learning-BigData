################
#### PRESTO ####
################

Distributing queries across different data stores.

#### What is Presto ?

- It's a lot like Drill
    * It can connect to many different "big data" databases and data stores at once, and query across them.
    * Familiar SQL syntax
    * Optimized for OLAP- analytical queries, data warehousing
- Developed and still partially maintained by Facebook.
- Exposes JDBC, Command-Line and Tableau intefaces.

#### Why Presto?

- Vs. Drill? Well, it has a cassandra connector for one thing.
- If it's good enough for FaceBook
        * "Facebook uses Presto for interactive queries against several internal data stores, including their 300PB data warehouse.
          Over 1,000 Facebook employees use Presto daily to run more than 30,000 queries that in total scan over a petabyte each per day."
        * Also used by DropBox and AirBNB
- " A single Presto query can combine data from multiple sources, allowing for analytics across your entire organization."
- " Presto breaks the false choice between having fast analytics using an expensive commerical solution or using a slow "free"
    solution that requires excessive hardware."
    
#### What can Presto connect to ?

- Cassandra (It's Facebook, after all)
- Hive 
- MongoDB 
- MySQL
- Local Files
- And stuff we haven't talked about just yet:
    * Kafka, JMX, PostgresSQL, Redis, Accumlo.
    
#### List To Do

- Set up Presto
- Query our hive ratings table using Presto
- Spin Cassandra back up, and query our users table in Cassandra with Presto.
- Execute a query that joins users in Cassandra with ratings in Hive!

#### Install Presto, and qyery Hive with it

1.  Login to hadoop virtual machine.

2.  su root

3.  pwd

4.  wget https://repo1.maven.org/maven2/com/facebook/presto/presto-server/0.165/presto-server-0.165.tar.gz

5.  tar -xvf presto-server-0.165.tar.gz

6.  ls

7.  cd presto-server-0.165

8.  ls

9.  pwd

10. wget http://media.sundog-soft.com/hadoop/presto-hdp-config.tgz

12. tar -xvf presto-hdp-config.tgz

13. ls

14. cd bin

15. wget https://repo1.maven.org/maven2/com/facebook/presto/presto-cli/0.165/presto-cli-0.165-executable.jar

16. mv presto-cli-0.165-executable.jar presto

17. chmod +x presto

18. cd ..

19. bin/launcher start

20. Go to UI 127.0.0.1:8090

21. bin/presto --server 127.0.0.1:8090 --catalog hive

  > show tables from default;
  
  > select * from default.ratings limit 10;
  
  > select * from default.ratings where rating = 5 limit 10;
  
  > select count(*) from default.ratings where rating=1;
  
  > quit
  
22. bin/launcher stop\

#### query cassandra and hive using presto

- scl enable python27 bash

- python -V

- service cassandra start

- nodetool enablethrift 

- cqlsh --cqlversion="3.4.0"

 > describe keyspaces;
 
 > use movielens;
 
 > describe tables;
 
 > select * from users limit 10;
 
 > quit
 
 - cd etc/catlog
 
 - nano cassandra.properties
      connector.name = cassandra
      cassandra.contact-points=127.0.0.1
      
 - cd ../..
 
 - bin/launcher start
 
 - bin/presto --server 127.0.0.1:8090 --catalog hive,cassandra
 
  > show tables from cassandra.movielens;
  
  > describe cassandra.movielens.users;
  
  > select * from hive.default.ratings limit 10;
  
  > select u.occupation, count(*) from hive.default.ratings r join 
    cassandra.movielens.users u on r.user_id = u.user_id group by u.occupation;
    
  > quit
  
  - bin/launcher stop
  
  - service cassandra stop
  
