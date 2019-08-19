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
  Note: Target table must be exist in MySQL with expected column order. For examples: please use the data from data folder.
  
  In Hadoop virtual machine, follow the following steps:
  1. $ mysql -u root -p
     pwd: hadoop
  2. $ exit.
  3. $ wget http://media.sundog-soft.com/hadoop/movielens.sql .
  4. #import moviedata in MySQL:
  
     $ mysql -u root -p
  6. mysql>  SET NAMES 'utf8';
 
     mysql>  SET CHARACTER SET utf8;
     
          >  use movielens;
          
          >  source movielens.sql;
          
          >  show tables;
          
          >  select * from movies limit 10;
  
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
  11.$ Sqoop import --connect jdbc://mysql://localhost/movielens --driver com.mysql.jdbc.Driver --table movies -m 1 --hive-import
  12.$ mysql -u root -p
  13. pwd:hadoop
  
      > use movielens;
      
      > CREATE TABLE exported_movies(id INTEGER, title VARCHAR(255), releaseData DATE);
      
  14. $ exit
  15. $ sqoop export --connect jdbc:mysql://localhost/movielens -m 1 --driver com.mysql.jdbc.Driver --table exported_movies --export -dir /apps/hive/warehouse/movies --input-fields-terminated-by '\0001'
  
  NOTE: For incremental imports:
  
      - keep realtional DB & Hadoop in sync.
      
      $ --check -column and --last -value
