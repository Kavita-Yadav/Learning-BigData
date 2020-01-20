# HDFS and MapReduce

#####################
###### HDFS #########
#####################
 - HDFS helps to handle big files by breaking them into block.
 - Stored across several commodity computer.
 
 **HDFS ARCHITECTURE**
 
- There will be one Namenode as master and multiple Datanode as slave.

![HDFS Architecture](https://github.com/Kavita-Yadav/Learning-Hadoop-and-bigData/blob/master/HDFS-and-MapReduce/HDF_Architecture.png)


**How to read a file in HDFS ?**

![HDFS FileRead](https://github.com/Kavita-Yadav/Learning-Hadoop-and-bigData/blob/master/HDFS-and-MapReduce/HDFSFileRead.png)

- Clientnode will first ask for file information from Namenode. Namenode will give the all details of file, 
- for example: where is the file? what is the name of file ? etc. 
- Clientnode will get the information and will retrieve the file from defined path. 
- For example: file is at DataNode2. Then client node will fetch the file from DataNode2.

**How to write a file in HDFS ?**

Step 1:

    1. Client Node  -----> Name Node
    - Clientnode will first ask to Namenode to create a new entry.
    - Namenode will acknowledge than entry created and now I have started to track this file.
    
Step 2:

    2. Client Node ------> Data Node 1
    - Clientnode then create a file on Data Node.

Step 3:

    3. DataNode1 ----> DataNode2 ----> DataNode3
    - DataNode1 will tell to other Datanodes to replicate file on each block of Datanode2 & Datanode3.

Step 4:

    4. DataNode3 -----> DataNode2 -------> DataNode1 ------> ClientNode-----> NameNode
    - DataNode will acknowlege back to NameNode that everything is working perfectly via ClientNode
    - Now, NameNode will create a record for new file created.

**Backup MetaData in HDFS**
- NameNode write to local disk and NFS

**Secondary NameNode**
- It will maintain merge copy of edit log from primary name node that you can restore.

**HDFS Federation**
- Each namenode manages a specific namespace volume. If any name node will get down then it will not loose all data.

**HDFS High Availability**
- Hot standby namenode using shared edit log. if namenode gets down, another namenode will get start.
- Zookeeper tracks active namenode.
- Uses extreme measures to ensure that only one namenode is used at a time.

**How to use HDFS ?**
- UI(Ambari)
- Command Line Interface
- HTTP/HDFS Proxies
- Java Interface
- NFS Gateway


#######################
###### MAPREDUCE ######
#######################
- MapReduce distributes processing of data on cluster.
- Divides your data up into partition that are MAPRED(transformed) & REDUCED(aggregated) by mapper & reducer function we define.
- Resilient to failure.

        DataSet ----> Mapper ----> Shuffle & Sort ----> Reducer

**MapReduce Working**
- MAPPER conver raw source data into key/value pairs.

      InputData ---> Mapper ----> k1:v k2:v k3:v
      
Let's understand it with example:
we have a Table with Movie Rating Data.
 _______________________________________
| userID | movieID | rating | timestamp |
 _______________________________________
| 196    | 242     | 3      | 88123     |
| 186    | 302     | 3      | 88124     |
| 196    | 377     | 1      | 88125     |
| 244    | 51      | 2      | 88126     |
| 166    | 346     | 1      | 88127     |
| 186    | 474     | 4      | 88128     |
| 186    | 265     | 2      | 88129     |
 _______________________________________
 
1. Map users to movies they have watched. For Mapper function; There are two coloumn which consist valuable information for mapper i.e UserID and MovieID.
2. Output from Mapper will be:      
             _i196:242  186:302  196:377  244:51  166:346  186:474  186:265i_
3. Extract and organize whatever information needed.

- MapReduce sorts and groups the mapped data using SHUFFLE & SORT.

1. Output from shuffle and sort will be:
            _i196:242  186:302  196:377  244:51  166:346  186:274  186:265i_
                                          |
            _i166:346  186:302,274,265  196:242,377  244:51i_
- REDUCER process each key's value using len() function.
           _i166:346  186:302,274,265  196:242,377  244:51i_
                                 | len(movies)
                   _i166:1   186:3   196:2  244:1i_
                   
**MapReduce on Cluster**
              
       ClientNode --- Yarn Resource Manager ----- Node Manager(MapReduce Application Master)
                                                            /                        \
                 HDFS--------------------------NodeManager Node                    NodeManager
                  | |                  (Map/Reduce Task | Map/Reduce Task)       (Map/Reduce Task)
                  | |                            |                                      |
                  | '----------------------------'                                      |
                  |                                                                     |
                  '---------------------------------------------------------------------'
                  
**How mapper & reducer written ?**
- MapReduce is natively Java.
- Streaming allow interacting to other language(i.e python).

                   MapTask/ReduceTask
                     |           ^
                stdin| key/value |stdout
                     |           |
                   Streaming Process
                 
**Handling Failure**
- Application master monitors worker tasks for error. Restart when needed on different nodes.
- If application master goes down, Yarn can try to restart it.
- If entire node goes down,it could be the application master and resource manager will try to restart it.
- If resource manager goes down, set up 'High Availability(HA)' using Zookeeper to have a hot standby.

_iExample of MapReduce for Movie Ratings data in python using above datatable:i_

1. Map each input line to (rating,1)
2. Reduce each rating with sum of all the 1's.

       Rating: 3 3 1 2 1 4 2
                | map
       (3,1) (3,1) (1,1) (2,1) (1,1) (4,1) (2,1)
                | shuffle & sort
       1-> 1,1  2-> 1,1  3-> 1,1  4-> 1
                | reduce
       1,2  2,2  3,2  4,1

 
 **Runing MapReduce with MRJobs**
 1. Start virtual box hadoop machine.
 2. Login via terminal by following command ' ssh maria_dev@127.0.0.1 -p 2222 '
 3. pwd: maria_dev
 4. su root
 5. pwd: hadoop
 6. If HDP 2.6.5, run following commands:
    - yum install python-pip
    - pip install mrjob==0.5.11
    - yum install nano

 7. If HDP 2.5, run following commands:
    - cd /etc/yum.repos.d
    - cp sanbox.repo /tmp
    - rm sandbox.repo
    - cd ~
    - yum install python-pip
    - pip install google-api-python-client==1.6.4
    - pip insatll mrjob==0.5.11
    - yum install nano
 8. wget https://github.com/Kavita-Yadav/Learning-Hadoop-and-bigData/blob/master/HDFS-and-MapReduce/MRJobExample.py
 9. If run locally, use command 'python MRJobExample.py u.data'.
10. If run with hadoop, use command ' python MRJobExample.py -r hadoop --hadoop-streaming-jar 
     /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar u.data '.
