## What is HBase ?
- It is non-realtional scalable database built on HDFS.
- Just like other NoSQL solution, it does not have a query language but it does have an API that can very quickly answer the question.
- It built on the idea behind google's BigTable databae. HBase is preety much an implementaion of the algorithms and systems 
described in BigTable.It is an open source implementation of the algorithm and systems described im BigTable.
- It does not have a query language equivalent of SQL, it just has an API, so it can call CRUD(Create, Read, Update, Delete) operations.
- CRUD: Creating a row in a database, reading back the values of a row in a database, updating a row in a database, or deleting a row in
a database.
- But it is very quick and does CRUD at very large scale.

## HBase Architecture:

             _________________           ________________
            |    Zookeeper    |         |    HMaster     |
             _________________           ________________
          
    
    
           ________      ________     ________     ________
          | Region |    | Region |    | Region |   | Region |
          | Server |    | Server |    | Server |   | Server |
           ________      ________      ________      _______
                                                                  Auto-sharding!
            ________________________________________________
           |                     HDFS                       |
            ________________________________________________
      
      - Zookeeper can keep track of who the current master server is for your HBase instance.
      - It's partitioned amongest different region servers. There is master server who track that 
        where everything is and data itself is actually stored on big files on HDFS.
      - If master goes down, zookeeper can keep track of who to go to next and tell everyone that 
        who the master is now.
      
## HBase data model:

  - Fast access to any given ROW.
  - A ROW is referenced by a unique KEY.
  - Each ROW has some small number of COLUMN FAMILIES.
  - A COLUMN FAMILY may contain arbitrary COLUMNS.
  - You can have a very large number of COLUMNS in a COLUMN FAMILY.
  - Each CELL can have many VERSIONS with given timestamps.
  - Sparse data is A-OK- missing columns in a row consume no storage.
  
## Example: One row of a web table:
  
  ![HBase Example](https://github.com/Kavita-Yadav/Learning-Hadoop-and-bigData/blob/master/Images/Example_HBase.png)
       
       
    - Wants to track all the links that connect to a given web page. Trying to figure out who links back to CNN.com.
    - They might have key that is a web page or web site and they actually store this in reverse order.
    - So instead of www.CNN.com, they do it backwards in com.CNN.www.
    - Reason is that keys are stored lexicographically withi HBase.
    - They set couple of column family in this example. Contents column family and there's only one column within this column
      family- "Contents" itslef. The are using the versioning feature to actually keep three copies of the contents of this page.
    - They are actually scraping CNN.com and storing the last three incarnations of that page.
    - In Anchor column family, they are storing all of the pages on the web that link back to CNN.com .
    - Anchor:cnnsi.com represent a link from cnnsi.com and anchor.
    
## Some ways to access HBase
- HBase shell
- Java API: wrappers for Python,scala, stc.
- Spark, Hive, Pig
- REST service
- Thrift sservice
- Avro service

## Practical Implementation:
   Creating a HBase table with Python via REST
    
   _iWhat are we doing?i_
   
   - create a HBase table for movie ratings by user.
   - Then show we can quickly query it for individual users.
   - Good example of sparse data:
                                  Column family: rating
                            Rating:50     Rating:33     Rating:233
           UserID               1             5             5
           
   _iHow are we doing it?i_
   
                            Python client
                                  |
                            REST service
                                  |
                                 \|/
                              ________
                             | HBase  |
                              ________
                             |  HDFS  |
                              ________
     
       
   1. Login to Hadoop virtual machine.
   2. Go to Settings->General->Network->Advanced->Port Forwarding Rules.
   
        Name: HBaseREST, Protocol: TCP, Host_IP: 127.0.0.1, Host_Port: 8000, Guest_IP: - , Guest_Port: 8000
   3. Login to Ambari dashboard as admin user.
   4. Go to "HBase" service. Click on Service Actions-> Start->Confirm Start->OK.
   5. Goto virtual machine now. $ su root.
   6. $ /usr/hdp/current/hbase-master/bin/hbase-daemon.sh start rest -p 8000 --infoport 8001
   7. $ pip install starbase
   8. $ Python HBase.py
   10.$ /usr/hdp/current/hbase-master/bin/hbase -daemon.sh stop rest
   
  ## Starbase
  - "from starbase import Connection" helps to create connections.
  - Create connection instance:
      c = connection(IP, Port).
      eg: c = connection("127.0.0.1", "8000")
  - Show tables:
      c.tables('table_name')
      eg: c.tables('ratings')
  - Create table insrance:
      t = c.table('table_name')
      eg: ratings = c.table('ratings')
  - Create new table:
      t.create('column 1' , 'column 2', column 3')
      eg: ratings.create('rating')
  - Check if table exists:
      t.exists('table_name')
  - Show table columns:
      t.columns('table_name')
  - add columns to table:
      t.add_columns('col_name 1', 'col_name 2')
  - drop columns from table:
      t.drop_columns('col_name 1', 'col_name 2')
  - drop entire table schema:
      t.drop('table_name')
  - Packages:
      starbase.client.connection.Connection
      (cluster_version, cluster_status, drop_table, tables, table_exists, version)
      
      starbase.client.table.Table
      (add_columns, batch, create, drop, drop_columns, exists, insert, fetch, fetch_all_rows, regions, remove, schema, upadte)
      
      starbase.client.table.Batch
      (commit, insert, upadte)
      
      starbase.client.transport.HttpRequest
      eg: connection.version
      
      Failed requests:
      retries(int), retry_delay(int)
      eg: c = connection(
              retries = 3 #Retry 3 times
              retry_delay = 5 # wait for 5 seconds b/w retries)
              
       Note: no. of retries can acuse performance issues in your application.
       
  ## Use HBase with Pig to Import data at scale:
      1. First need to integrate pig with HBase.
      2. Create HBase tbale ahead of time.
      3. Your realtion must have a unique key at its first column,followed by subsequent columns as you want them saved in HBase.
      4. USING clause allows you to STORE into HBase table.
      5. Can work at scale-HBase is transactional on rows.
      6. Go to ambari->FileView -> user-> maria_dev-> ml-100k.
      7. upload "u.user" data file.
      8. Login to hadoop sandbox.
      9. $ su root
      10.$ hbase shell
         > list
         > create 'users', 'userinfo'
         > exit
      11.$ wget http://media.sundog-soft.com/hadoop/hbase.pig .
      12.$ less hbase.pig
      13.$ pig hbase.pig
      14.$ hbase shell
         > list
         > scan users
         > disable 'users'
         > drop 'users'
         > list
         > exit
      15.$ exit
      16. Shutdown HBase service:
          Go to Ambari.
          Click 'services'
          Click 'HBase'
          Click 'Service Actions' -> Stop.
