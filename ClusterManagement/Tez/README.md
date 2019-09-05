####################
#### APACHE TEZ ####
####################

- Directed Acyclic Graph Framework

#### What is TEZ ?
- Another bit of infrastructure you can just use
    * Makes you rHIve, Pig, or MapReduce jobs faster!
    * It'a an application framework clients can code against as a replacement fro MapReduce.
- Constructs Directed Acyclic Graphs (DAGs) fro more efficient processing of distributed jobs
    * Relies on a more holistic view of you rjob; eliminates unnecessary steps and dependencies.
- Optimizes physical data flow and resource usage.

#### Directed Acyclic Graphs:

            Map   Map   Map
             \    /\     /            Map   Map                     Map   Map    Map 
              \  /  \   /               \   /                        \    /\     / 
            Reduce  Reduce              Reduce                        \  /  \   /
        HDFS---|------|---HDFS            /                          Reduce Reduce                  Map     Map
              Map    Map                 /                              \     /                       \     /
                \    /                  /                                \   /                          \ /
                Reduce                 /                                 Reduce                        Reduce
                   \                  /                                       \                        /
          HDFS ---- \--------------  / ---- HDFS                                \                     /  
                    Map            Map                                            \                 /
                      \            /                                                \             /
                       \          /                                                   \         /
                         \       /                                                      \     /
                          Reduce                                                        Reduce

                  #### Pig/Hive - MR                                            #### Pig/Hive - Tez
    
   Notice that Tez don't use HDFS and skipped mapper tasks which we need to use in MR.
