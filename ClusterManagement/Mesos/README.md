###############
#### MESOS ####
###############

- Yes, yet anotherr resource negotiator.

#### What is Mesos ?

- Came out of Twitter - it's a system that manages resources across your data center(s).
- Not just for big data stuff- it can allocate resources for web servers, small scripts, whatever.
- Meant to solve a more general problem than YARN - it's really a general container management system.
- Mesos isn't really part of the Hadoop ecosystem oer se, but it can play nice with it
    * Spark and Storm may both run on Mesos instead of YARN.
    * Hadoop YARN may be integrated with Mesos using Myriad.
        - So you don't necessarily need to partition your data center between your Hadoop cluster and everything else!
        
#### Difference between Mesos and YARN:

- YARN is monolithic scheduler - you give it a job, and YARN figures out where to run.
- Mesos is a two-tired system.
    * Mesos just makes offers of resources to your application ("framework")
    * your framework decides whether to accept or reject them
    * You also decide your own scheduling algorithm
- YARN is optimized for long, analytical jobs like you see in Hadoop.
- Mesos is built to handle that, as well as long-lived processes(servers) and short-lived process as well.

#### How Mesos fits in ?

- If you're looking for an architecture you can code all of your organization's cluster applications against - not just
  Hadoop stuff - Mesos can be really useful.
    * You should also look at Kuberentes / Docker
- If all you are about is Spark and Storm from the Hadoop-y world, Mesos is an option
    * But YARN's probably better, especially if your data is on HDFS
    * Spark on Mesos is limited to on executor per slave (node)
    
    
 #### Siloed vs resource sharing:

        Siloed:
                      ________________                             _______________
                     |     Mesos      |                           |     YARN      |
                     |________________|                           |_______________|
                     |    Framework   |                           |   Resource    |
                     |       +        |                           |    Manager    |
                     |      master    |                           |               |
                      ________________                             _______________

           _______________________________________       _______________________________________
          |  ________________  _________________  |     |  ________________  _________________  |
          | |     Node       ||     Node        | |     | |     Node       ||     Node        | |
          | |________________||_________________| |     | |________________||_________________| |
          | |    M     M     ||    M       M    | |     | |    Y     Y     ||    Y       Y    | |  
          | |    M     M     ||    M       M    | |     | |    Y     Y     ||    Y       Y    | |  
          |  ________________  _________________  |     |  ________________  _________________  |
          |  ________________  _________________  |     |  ________________  _________________  |
          | |     Node       ||     Node        | |     | |     Node       ||     Node        | |
          | |________________||_________________| |     | |________________||_________________| |
          | |    M     M     ||    M       M    | |     | |    Y     Y     ||    Y       Y    | |  
          | |    M     M     ||    M       M    | |     | |    Y     Y     ||    Y       Y    | |  
          |  ________________  _________________  |     |  ________________  _________________  |
           _______________________________________        ______________________________________
           
           
         Resource Sharing:  
                      ________________                             _______________
                     |     Mesos      |                           |     YARN      |
                     |________________|                           |_______________|
                     |    Framework   |                           |   Resource    |
                     |       +        |                           |    Manager    |
                     |      master    |                           |               |
                      ________________                             _______________

           _______________________________________       _______________________________________
          |  ________________  _________________  |     |  ________________  _________________  |
          | |     Node       ||     Node        | |     | |     Node       ||     Node        | |
          | |________________||_________________| |     | |________________||_________________| |
          | |    M     M     ||    Y       Y    | |     | |    M     Y     ||    Y       Y    | |  
          | |    M     M     ||    Y       Y    | |     | |    Y     M     ||    Y       Y    | |  
          |  ________________  _________________  |     |  ________________  _________________  |
          |  ________________  _________________  |     |  ________________  _________________  |
          | |     Node       ||     Node        | |     | |     Node       ||     Node        | |
          | |________________||_________________| |     | |________________||_________________| |
          | |    Y     Y     ||    M       M    | |     | |    Y     Y     ||    M       M    | |  
          | |    Y     M     ||    M       M    | |     | |    Y     Y     ||            M    | |  
          |  ________________  _________________  |     |  ________________  _________________  |
           _______________________________________        ______________________________________
           
                                            M- Mesos   Y- Yarn
                                            
 #### When to use Mesos ?
 
 - If your organization as a whole has chosen to use Mesos to manage its computing resources in general
    * Then you can avoid partitioning off a Hadoop cluster by using Myriad
    * There is also a "Hadoop on Mesos" package for Cloudera that bypasses YARN entirely.
 - Otherwise - probably not. I just want you know what Mesos is and how it's different from YARN.
