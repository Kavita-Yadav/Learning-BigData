#####################
#### HADOOP YARN ####
#####################

What is YARN?
- Yet Another Resource Negotiator
    * Introduced in Hadoop 2
    * Separates the problem of managing resources on your cluster from
    * Enabled development of MapReduce alternatives (Spark, Tez) built on top of YARN
    
Where YARN fits in ?

              ___________      ________      _________
             | MapReduce |    | Spark  |    |   Tez   |       YARN Applications
              ___________      ________      _________
              _________________________________________
             |                 YARN                    |      Cluster Compute Layer
              _________________________________________
              _________________________________________
             |                 HDFS                     |     Cluster Storage Layer
              _________________________________________
    
Remember how MapReduce works:

            _____________                ___________           _____________
           | Client Node |--------------|   YARN    |         | NodeManager |
            _____________               |  Resource |         |_____________|
                |                       |  Manager  |         |  MapReduce  |
                |                        ___________          | Application |
                |                                             |   Master    |
                |                                              _____________
                |                                                 /     \
             _______                                             /        \
            | HDFS  |                               _______________________      ______________
             _______  \----------------------------| NodeManager Node      |    | NodeManager  |
                       |                           |_______________________|    |______________|
                       |                           |MapTask/   |MapTask/   |    |  MapTask/    |
                       |                           |ReduceTask |ReduceTask |    | ReduceTask   |
                       |                            _______________________      ______________
                       |                                  |                            |
                       |----------------------------------|                            |
                       |                                                               |
                       |________________________________________________________________
