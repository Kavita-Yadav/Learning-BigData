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
  
              key          Contents column family                Anchor column family 
                            Contents:                      Anchor:cnnsi.com  Anchor:my.look.ca
       | com.cnn.www |    |  <html><head> CNN....|     | "CNN" |           | "CNN.com" |
       
       
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

## Practical Implementaion:
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
