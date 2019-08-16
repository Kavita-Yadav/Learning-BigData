###############
#### Sqoop ####
###############

Used to integrate MySQL and Hadoop. Before heading forward just a quick review about MySQL for those, who are not known to MySQL.

## What's MySQL ?
- Popular, free relational database.
- Generally monolithic in nature.
- But, can be used for OLTP= so exporting data into MySQL can be useful.
- Existing data may exist in MySQL that you want to import to Hadoop.

## Sqoop: 
- Sqoop can handle BIG data.
- It helps to rescue from import data from MySQL to Hadoop, Which actually kicks off MapReduce jobs to handle 
importing or exporting your data.
              
              
                                     ____________
                                    |   MySQL/   |
                                    |  PostGres/ |
                                    |  whatever  |
                                     ____________
                                     /    |     \
                                    /     |      \
                                Mapper  Mapper  Mapper
                                   \      |      /
                                     \    |    /
                                    ______________
                                   |     HDFS     |
                                    ______________
                                    
  
 ## How to use sqoop ?
