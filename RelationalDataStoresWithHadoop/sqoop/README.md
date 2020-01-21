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

![Sqoop Architecture](https://github.com/Kavita-Yadav/Learning-Hadoop-and-bigData/blob/master/RelationalDataStoresWithHadoop/sqoop/SqoopArchitecture.png)                        
  
 ## How to use sqoop ?
  Note: Target table must be exist in MySQL with expected column order. For examples: please use the data from data folder.
  
  In Hadoop virtual machine, follow the following steps:
  1. $ mysql -u root -p
  
     pwd: hadoop
     
     > create database movielens;
  2. $ exit.
  3. $ wget http://media.sundog-soft.com/hadoop/movielens.sql .
  4. #import moviedata in MySQL:
  
     $ mysql -u root -p
     
     pwd: hadoop
  6. mysql>  SET NAMES 'utf8';
 
          >  SET CHARACTER SET utf8;
     
          >  use movielens;
          
          >  source movielens.sql;
          
          >  show tables;
          
          >  select * from movies limit 10;
          
          >  describe ratings;
  
          >  SELECT movie.title, COUNT(ratings.movie_id) AS ratingCount 
          
          >  FROM movies
          
          >  INNER JOIN ratings
          
          >  ON movies.id = ratings.movie_id
          
          >  GROUP BY movies.title
          
          >  ORDER BY ratingCount;
          
          >  exit
          
  7. #Use sqoop to import data from MySQL to HDFS/HIve
  
      $ mysql -u root -p 
        pwd: hadoop
        > GRANT ALL PRIVILEGES ON movilens.* to ''@'localhost';
  9. $ exit
  10.$ Sqoop import --connect jdbc:mysql://localhost/movielens --driver com.mysql.jdbc.Driver  --table movies -m 1
  
      ( Can see the ouput on ambari window in FileView: user>maria_dev>movies>part-m-00000 )
  11.$ Sqoop import --connect jdbc://mysql://localhost/movielens --driver com.mysql.jdbc.Driver --table movies -m 1 --hive-import
  
      ( Can see the ouput in HiveView: default Database; there is movies table exist now)
  12.$ mysql -u root -p
  13. pwd:hadoop
  
      > use movielens;
      
      > CREATE TABLE exported_movies(id INTEGER, title VARCHAR(255), releaseData DATE);
      
  14. $ exit
  15. $ sqoop export --connect jdbc:mysql://localhost/movielens -m 1 --driver com.mysql.jdbc.Driver --table exported_movies --export-dir /apps/hive/warehouse/movies --input-fields-terminated-by '\0001'
  
  NOTE: For incremental imports:
  
      - keep realtional DB & Hadoop in sync.
      
      $ --check -column and --last -value
