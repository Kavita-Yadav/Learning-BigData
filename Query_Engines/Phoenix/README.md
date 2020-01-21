#######################
#### Apache Phonix ####
#######################

- SQL for HBase

#### What is Phoenix ?

- A SQL driver for HBase that supports transactions.
- Fast, low-latency- OLTP support.
- Originally developed by Salesforce, then open-sourced.
- Exposes a JDBC connector for HBase.
- Supports secondary indices and user-defined functions.
- Integrates with MapReduce, Spark, Hive, Pig and Flume.

#### Why Phoenix?

- It's really fast. You probably won't pay a performance cost from having this extra layer on top of Hbase.
- Why Phoenix not Drill ? well, choose the rightt tool for the job.
- Why Phoenix and not HBase's native clients ?
  Your apps, and analysts, may find SQL easier to work with.
  Phoenix can do the work of optimizing more complex queries for you
   - But remember HBase is stil fundamentally non-relational!
   
#### Phoenix architecture:

![Phoenix Architecture](https://github.com/Kavita-Yadav/Learning-Hadoop-and-bigData/blob/master/Images/PhoenixArchitecture.png)

                    
 #### Using Phoenix:
 - Command-Line Interface (CLI).
 - Phoenix APi for Java.
 - JDBC Driver (thick Client).
 - Phoenix Query Server (PQS) (thin client).
    Intended to eventually enable non-JVM access.
 - JAR's for MapReduce, Hive, Pig, Flume, Spark.
 
 #### TO DO List for Phoenix:
 - Install Phoenix on our Hortronworks Sandbox.
 - Mess around with the CLI.
 - Set up a users table for MovieLens.
 - Store and load data to it through the Pig integration.
 
 #### Install Phoenix:
 1. Start HBase service in Ambari UI.
 
 2. yum install phoenix.
 
 3. cd /usr/hdp/current/phoenix-client/
 
 4. ls
 
 5. cd bin
 
 6. python sqlline.py
 
 7. Run query in terminal jdbc:phoenix:> 
  
              CREATE TABLE IF NOT EXISTS us_population(
              state CHAR(2) NOT NULL,
              city VARCHAR NOT NULL,
              population BIGINT
              CONSTRAINT my_pk PRIMARY KEY (state, city));
              
  > !tables.
  
  > UPSERT INTO US_POPULATION VALUES ('NY', 'New York', 8143197);
  
  > UPSERT INTO US_POPULATION VALUES ('CA', 'Los Angeles', 3844829);
  
  > SELECT * FROM US_POPULATION;
  
  > SELECT * FROM US_POPULATION WHERE STATE = 'CA';
  
  > DROP TABLE US_POPULATION;
  
  > !tables
  
  > !quit
  
  
 #### Integrate Phoenix with Pig
 
 $ pwd
 
 $ python sqlline.py
 
 > CREATE TABLE users (USERID INTEGER NOT NULL, AGE INTEGER, GENDER CHAR(1), OCCUPATION VARCHAR, ZIP VARCHAR CONSTRAINTT pk
  PRIMARY KEY(USERID));
  
 > !tables
 
 > !quit
 
 $ cd /home/maria_dev
 
 $ ls
 
 $ mkdir ml-100k
 
 $ cd ml-100k/ 
 
 $ wget http://media.sundog-soft.com/hadoop/ml-100k/u.user
 
 $ cd ..
 
 $ pwd
 
 $ wget https://github.com/Kavita-Yadav/Learning-Hadoop-and-bigData/blob/master/Query_Engines/Phoenix/Phoenix.pig
 
 $ pig phoenix.pig
 
 $ cd /usr/hdp/current/phoenix-xlient/bin
 
 $ python sqlline.py
 
 > !tables
 
 > SELECT * FROM USRES LIMIT 10;
 
 > DROP TABLE users;
 
 > !tables
 
 > Stop HBase service from Ambari UI.
 
 
 
 
                             
                              
