###################
#### ZooKeeper ####
###################

#### What is ZooKeeper ?

- It basically keeps track of information that must be synchronized across your cluster
    * Which node is the master ?
    * What tasks are assignes to which workers?
    * Which workers are currently available?
- It's a tool that applications can use to recover from partial failures in your cluster.
- An integral part of HBase, High-Availabiltiy (HA) MapReduce, Drill, Storm, Solr, and much more.

#### Failure modes in which ZooKeeper can help ?
* It will get to know if Master, Worker or Network crashes.
  - Master crashes, needs to fail over to a backup.
  - Worker crashes - its work needs to be redistributed.
  - Network trouble - part of your cluster can't see the rest of it.

                            Master
                          
                  Worker    Worker    Worker    
 
 * "Primitive' operations in a distributed system:
    - Master election
       - One node registers itself as a master, and holds a "lock" on that data.
       - Other nodes cannot become master until that lock is released.
       - Only one node allowed to hold the lock at a time.
    - Crah detection
       - "Ephemeral" data on a node's availability automatically goes away if the node disconnects, or fails to refresh itself
          after some time-out period.
    - Group management
       - What workers are available in pool.
    - Metadata
       - List of outstanding tasks, task assignments.
 * But zooKeeper's API is noy about these primitives.
    - Instead they have built a more general purpose system that makes it easy fro applications to implement them.
 
 #### ZooKeeper's API
 - Really a little distributed file system.
    * With strong consistency guarantees.
    * Replace the concept of "file" with "znode" and you've pretty much got it.
 - Here's the ZooKeeper API:
    * Create, delete, exists, setData, getData, getChildren
    
                  /
                  |
                  |------ /master   "master1.foobar.com:2223"
                  |
                  |------ /wrokers
                              |
                              |----- worker-1 "worker-2.foobar.com:2225"
                              |
                              |----- worker-2 "worker-5.foobar.com:2225"
           
 #### Notifications:
 - A client can register for notifications on a znode
    * Avoids continous polling.
    * Example: register for notification on/master - if it goes away, try to take over as the new master.
    
 #### Persistent and ephemeral znodes:
 - Persistent znodes remain stored until explicitly deleted.
      - i.e, assignment of tasks to workers must persist even if master crashes.
 - Ephemeral znodes go away of the client that created it crashes or loses its connection to ZooKeeper.
      - i.e, if the master crashes, it should release its lock on the znode that indicates which node is the master!
      
 #### ZooKeeper Architecture:
 
                              __________                                     
                             |  Master  |                                    _____________________
                             |__________|                                   |   _______________   |
                             | ZK Client|                                   |  |   ZooKeeper   |  |
                              __________                                    |  |     Server    |  |
            __________        __________        __________                  |   _______________   |
           |  Worker  |      |  Worker  |      |  Worker  |                 |   _______________   |
           |__________|      |__________|      |__________|                 |  |   ZooKeeper   |  |
           | ZK Client|      | ZK Client|      | ZK Client|                 |  |     Server    |  |     ZooKeeper
            __________        __________        __________                  |   _______________   |     ensemble
                                                                            |   _______________   |   
                                                                            |  |   ZooKeeper   |  |
                                                                            |  |     Server    |  |
             Clients have a list of Zookeeper servers to connect to         |   _______________   |
                                                                            |   _______________   |
                                                                            |  |   ZooKeeper   |  |
                                                                            |  |     Server    |  |
                                                                            |   _______________   |
                                                                            |_____________________|
Note: If ZooKeeper goes down, we can use another ZooKeeper server. So there is ZooKeeper ensemble which has number of ZooKeeper server present in it. It is more of work like a monogoDB.
                         
#### Simulating a falling master with ZooKeeper:
- Login to terminal as maria_dev.
- su root
- cd /usr/hdp/current/zookeeper-cient/
- cd bin
- cd ./zkCli.sh
- [zk:localhost:2181 (CONNECTED) 0] ls /
- [zk:localhost:2181 (CONNECTED) 1] create -e /testmaster "127.0.0.1:2223"
- [zk:localhost:2181 (CONNECTED) 2] get /testmaster
- [zk:localhost:2181 (CONNECTED) 3] quit
- ./zkCli.sh
- [zk:localhost:2181 (CONNECTED) 0] ls /
- [zk:localhost:2181 (CONNECTED) 1] get /testmaster
- [zk:localhost:2181 (CONNECTED) 2] create -e /testmaster "127.0.0.1:2225"
- [zk:localhost:2181 (CONNECTED) 3] get /testmaster
- [zk:localhost:2181 (CONNECTED) 4] create -e /testmaster "127.0.0.1:2225"
- [zk:localhost:2181 (CONNECTED) 3] quit
- exit
- 


                         
