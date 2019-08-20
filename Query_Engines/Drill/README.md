###############
#### Drill ####
###############

#### Overview
- It is SQL for noSQL.
- It is basically lets you execute actual SQL queries on top of data that might not have schema at all.
- It certainly isn't realtional in nature.
- It's SQL engine that allows you to run realtional looking SQL queries accross a wide variety of non-relational database and data      files.
- Or in another words, A SQL query engine for a variety of non-relational databases and data files.
    - Hive, MangoDB, HBase.
    - Even flat JSON or Parquet files on HDFS, S3, Azure, Google cloud, local file system.
- Based on Google's Dremel.
- It's real SQL
      - Not SQL-Like
      - And it has a ODBC/JDBC driver so other tools can connect to ot just like any relational database.
- It's fast and pretty easy to set up.
- You can even do joins across different database techologies.

#### Steps for implementaion of drill:
- First, we will import data into Hive and MongoDB.
- Set up Drill on top of both.
- And do some queries!

#### Setting up Drill
- Login to Ambari as admin.
- Click on Services-> MongoDB-> Service Action-> Start-> Confirm Start-> Ok.
- Click on Hive View-> Query Editor.
  
      CREATE DATABASE movielens;
- Execute
- Click on Upload Table-> FileType: 9 TAB(horizontal tab) -> Choose File: u.data-> Stored as: ORC -> Table name: ratings.
- Change Column Name: Column1: user_id, Column2: movie_id, Column3: rating, Column4: epoch
- Click on Upload Table button.
- Go to Query Editor.
    
        SELECT * FROM ratings LIMIT 100;
