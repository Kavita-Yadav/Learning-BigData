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

   - **_Pig/Hive-MR_**
   
   ![Pig/Hive-MR](https://github.com/Kavita-Yadav/Learning-Hadoop-and-bigData/blob/master/Images/PigHiveMR.png)
   
   - **_Pig/Hive-Tez_**
   
   ![Pig/Hive-Tez](https://github.com/Kavita-Yadav/Learning-Hadoop-and-bigData/blob/master/Images/Tez.png)
    
   Notice that Tez don't use HDFS. Instead of dividing into different mapper reducer stages, It makes one sequence
   of dependencies and run it all together. That is why, It is lot faster.

#### Use Hive on Tez and measure the performance benefit:

- Login to Ambari
- Go to Hive View
- Upload Table-> choose CSV Field Delimiter: 124| -> Choose File(u.item) - > Table name: names
- Change column name : movie_id, name, release_date 
- Click on Upload Table now.
- Go to Query Editor. And write queries:

            DROP VIEW IF EXISTS topMovieIDs;
            
            CREATE VIEW topMovieIDs AS
            SELECT movie_id, coun(movie_id) as ratingCount
            FROM movielens.ratings
            GROUP BY movie_id
            ORDER BY ratingcount DESC;
            
            SELECT n.name, ratingCount
            FROM topMovieIDs t JOIN movielens.names n ON t.movie_id = n.movie_id;
            
 - Click on settings icon on right. Click on Add -> select 'hive.execution.engine' -> select value as 'tez'
 - Click on SQL and click on execute button to submit the query.
 - Click on settings icon on right. Click on Add -> select 'hive.execution.engine' -> select value as 'mr'
 - Click on SQL and click on execute button to submit the query.
 - Notice the time consume by both and analyze that which one is better by noticing there performance.
 - Click on Tez View.
 - Click on Dag Name of recent query run by you and see the details.
 - Click on DAG counters to see the counters name and value.
 - Click on Graphical View to see the DAG Graph.
