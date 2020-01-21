#####################
#### HADOOP YARN ####
#####################

#### What is YARN?
- Yet Another Resource Negotiator
    * Introduced in Hadoop 2
    * Separates the problem of managing resources on your cluster from
    * Enabled development of MapReduce alternatives (Spark, Tez) built on top of YARN
    
#### Where YARN fits in ?

              ___________      ________      _________
             | MapReduce |    | Spark  |    |   Tez   |       YARN Applications
              ___________      ________      _________
              _________________________________________
             |                 YARN                    |      Cluster Compute Layer
              _________________________________________
              _________________________________________
             |                 HDFS                     |     Cluster Storage Layer
              _________________________________________
    
#### Remember how MapReduce works:

![MapReduce](https://github.com/Kavita-Yadav/Learning-Hadoop-and-bigData/blob/master/Images/MapReduceOnCluster.png)
                       
#### YARN just generalizes this:
   
           _____________                ___________           _____________
           | Client Node |--------------|   YARN    |         | NodeManager |
            _____________               |  Resource |         |_____________|
                |                       |  Manager  |         |             |
                |                        ___________          | Application |
                |                                             |   Master    |
                |                                              _____________
                |                                                 /     \
             _______                                             /        \
            | HDFS  |                               _______________________      ______________
             _______  \----------------------------| NodeManager Node      |    | NodeManager  |
                       |                           |_______________________|    |______________|
                       |                           |Application|Application|    | Application  |
                       |                           |  Process  |  Process  |    |    Process   |
                       |                            _______________________      ______________
                       |                                  |                            |
                       |----------------------------------|                            |
                       |                                                               |
                       |_______________________________________________________________      
                       
                       
#### How YARN works:
 - Your application talks to the Resource Manager to distribute work to your cluster.
 - You can soecify data locality - which HDFS block(s) do you want to process ?
      * YARN will try to get your process on the same node that has your HDFS blocks.
 - You can specify different scheduling options for applications.
      * So you can run more than one application at once on your cluster.
      * FIFO, Capacity and Fair schedulers
         - FIFO runs jobs in sequenec, first in first out.
         - Capacity may run jobs in parallel if there's enough spare capacity.
         - Fair may cut into a larger running job if you just want to squeeze in a small one.
         
#### Building new YARN applications:

- Why? There are so many existing projects you can just use

      * Need a DAG*- based application? Build it on Spark or Tez
         - (*Directed Acyclic Graph)
- But if you really need to
      * There are frameworks: Apache Slider, Apache Twill
