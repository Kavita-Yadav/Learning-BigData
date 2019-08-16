##########################
#### Hadoop with Hive ####
##########################

There is various ways of integrating a new hadoop cluster with a MySQL database.One of them is Hive that make your new 
Hadoop cluster look like a realtional database.

## What is Hive?
- It is very powerful and simple way of querying data across your Hadoop cluster. 
- You will just write standard SQL queries thatlook just like using them on MySQL, but actually execute them on data 
  that's stored across your entire cluster. 
- It will translate your SQL query into MapReduce commands or Tezcommands, depending on your choice of selection. 
- It's break down your SQL query into mappers and reducers and figure out how to tie them all together and execute them
  across a cluster automatically.
- It is highly optimized and extensible. If SQL is not enough then you can actually plug in your own user-defined functions.
- It exposes the Thrift server, so you can actually talk to Hive from a service outside of Hive itself.
- It also exposes the JDBC and ODBC driver make Hive look just like any other database. 
- It's for OLAP(online analytics processing) not OLTP(online transaction processing).

## Drawbacks of Hive:
- High Latency- not appropriate for OLTP.
- Stores data de-normalized.
- SQL also has its limits. It can not seperate tables that are joined through foreign keys.
- For more complicated queries, you should use Pig or Spark.
- It's not a real database.
- It's just MapReduce under the hoos, don't have any transactions.
- Also there are no record level updates, inserts or deletes, because under the hood there are no real database records 
  to begin with. 
- It's just big flat text files that you're chugging through with mappers and reducers.

## HiveQL:
- It is similar to MySQL with some extensions.
- For example: views ; you can store results of ine query into a "view" and then use that "view" as a table in subsequent queries.
- It is different from the materialized view in the database world.
- Materialized view actually stores copies of the data but view in Hive is more of logical construct, It is not actually storing 
  a copy of data anywhere.
- HiveQL has bunch of extensions that allows you to specify that how the data you're reading in is structured and stored and 
  partitioned.
- In short, Except record-level stuff you can do with MySQL, similar you can do with HiveQL.

## How to run query in Hive ?
- Pull up Ambari on http://127.0.0.1:8080/ .
- Sign in with username: maria_dev pwd: maria_dev.
- Click on Grid next to Admin and go to "Hive View".
- Write a query in query editor and execute it by clicking on "Execute" button just like you write query in SQL.
- You can upload table in Hive by clicking on "Upload Table" -> select "File type".
- You can cutomize File type by clicking on "settings" icon. For example: for tab seprated value: 
      Change the "Field Delimeter" into " 9 TAB(horizontal tab)" and Close.
- Now, click on "Choose File" and select file from local machine and upload it. For example: select ml-100k/u.data file.
- Then, Write "Table name"; for example: ratings.
- Afterthat, give the name to "columns"; For example: userID, movieID, rating, epochseconds. You can also choose the data type of                    columns.
- Finally, click on "Upload Table".
- Another example for upload u.item file:
  Click on settings icon for cutomizing File type. Change Field Delimiter: 124 | (because data is sperated with pipe | in u.item        file.
- Choose File "u.item" from local machine ml-100k data folder
- Give Table name: names
- Change column name: movieID, title
- Click on Upload Table.
- Now write a query in query editiors.
- You can copy paste the scripts from .txt file into query editor to see how hive works.

## How Hive works ?
- It uses "schema on read" and "schema on write" approach. schema on write means where you write the schema of your database
  before load the data into it. Sometimes it enforced you to write data to disk.
- It take unstructured data and just sort of applies a schema to it as it's being read instead. So data is still stored as tab-delimited text files or whatever it might be with no actual structure to it.
- But Hive maintains a metastore, which is called as actual schema data that's associated with unstructured data.

_i Schema on Read: i_
* Basically, hive maintains a "metastore" that imparts a structure you define on the structured data that is stored on HDFS etc.
* For Example:
            
            CREATE TABLE ratings (
              userID INT,
              movieID INT,
              rating INT,
              time INT)
            ROW FORMAT DELIMTED
            FIELDS TERMINATED BY '\t'
            STORED AS TEXTFILE;
            
            LOAD DATA LOCAL INPATH '${env:HOME}/ml-100k/u.data'
            OVERWRITE INTO TABLE ratings;
            
_i Where is the data? i_
  * LOAD DATA
    - MOVES data from a distributed filesystem into Hive.
  * LOAD DATA LOCAL
    - COPIES data from your local filesystem into Hive.
  * Managed vs. External tables
  
        CREATE EXTERNAL TABLE IF NOT EXISTS ratings (
            userID INT,
            movieID INT,
            rating INT,
            time INT)
        ROW FORMAT DELIMITED FIELDS TERMINATED BY '\T'
        LOCATION '/data/ml-100k/u.data';
            
            
_i Partitioning: i_
 - you can store your data in partitioned subdirectories.
 - Huge optimization if your queries are only on certain partitions.
 
          CREATE TABLE customers (
            name STRING,
            address STRUCT<street:STRING, city:STRING, state:STRING, zip:INT>)
          PARTITIONED BY (country STRING);
          
          #STRUCTURE FOR THIS WOULD BE LIKE THIS:
              ..../customers/country=CA/
              ..../customers/country=GB/
              
 _i Ways to use Hive: i_
 - Interactive via hive> prompt/Command line interface(CLI).
 - Saved query files: _ihive -f /somepath/queries.hqli_
 - Through Ambari/Hue
 - Through JDBC/ODBC server
 - Through Thrift service, But remeber, Hive is not suitable fro OLTP.
 - Via Oozie.


