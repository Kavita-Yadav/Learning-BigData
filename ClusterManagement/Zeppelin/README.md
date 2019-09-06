##################
#### ZEPPELIN ####
##################

Notebook inteface to your data.

#### What is Zeppelin ?

- If you'rer familier with iPython notebooks- it's like that
      - Lets you interactively run scripts/code against your data.
      - Can interleave with nicely formatted notes.
      - Can share notebooks with othres on your cluster.
      
#### Apache Spark Integration
- Can run Spark code interactively (like you can in Spark shell).
    - This speeds up your development cycle.
    - And allows easy experimentation and exploration of your big data.
- Can execute SQL queries directly against SparkSQL.
- Query results may be visualized in charts and graphs.
- Makes Spark feel more like a data science tool!

#### Other interpreters that come with Zeppelin.
- Alluxio
- Google BigQuery
- Cassandra
- Elasticsearch
- Flink
- Apache Geode
- Apache HBase
- Hadoop HDFS
- Hive
- Apache Ignite
- Apache Lens
- Livy
- PostgreSQL
- Pyhton
- R
- Scalding
- Tajo

Note: Zeppelin comes pre-installed on Hortonworks Data Platform.

#### Use Zeppelin to analyze movie ratings:
- Login to Hadoop sandbox.
- Open Zeppelin UI browser 127.0.0.1:9995 .
- Create a new notebook "playing with data"
- %md
  ### Let's make sure Spark is working first!
  Let's see what version we're working first!
- sc.version
- %sh
  wget http://media.sundig-soft.com/hadoop/ml-100k/u.data -0 /tmp/u.data
  wget http://media.sundog-soft.com/hadoop/ml-100k/u.item -0 /tmp/u.item
  echo "Downloaded!"
- Copy data to HDFS
  %sh
  hadoop fs -rm -r -f /tmp/ml-100k
  hadoop fs -mkdir /tmp/ml-100k
  hadoop fs -put /tmp/u.data /tmp/ml-100k/
  hadoop fs -put /tmp/u.utem /tmp/ml-100k/
- final case class Rating(movieID: Int, rating:Int)
  
  val lines = sc.textFile("hdfs:///tmp/ml-100k/u.data").map(x=> {val fields = x.split("\t); Rating(fields(1).toInt, fields(2).toInt)})
- import sqlContext.implicits._
  
  val ratingsDF = lines.toDF()
  
  ratingsDF.printSchema()
- val topMovieIDs = ratingsDF.groupBy("movieID").count().orderBy(desc("count")).cache()
  
  topMovieIDs.show()
- ratingsDF.registerTempTable("ratings")
- %sql
  SELECT * FROM ratings LIMIT 10
- %sql
  SELECT rating, COUNT(*) as count FROM ratings GROUP BY rating
- final case class Movie(movieID: Int, title: String)
  val lines = sc.textFile("hdfs:///tmp/ml-100k/u.item").map(x => {val fields = x.split('|'); Movie(fields(0).toInt, fields(1))})
  
  import sqlContext.implicits._
  
  val moviesDF = lines.toDF()
  
  moviesDF.show()
- moviesDF.registerTempTable("titles")
- %sql
  SELECT t.title, count(*) cnt FROM ratings r JOIN titles t ON r.movieID GROUP BY t.title ORDER BY cnt DSC LIMIT 20
- %sql
  SELECT t.title, count(*) cnt FROM ratings r JOIN titles t ON r.movieID GROUP BY t.title ORDER BY cnt DSC
- Now go to new tab-> http://media.sundog-soft.com/hadoop/MovieLens.json
- Import Downloaded json file into Zeppelin using browser UI.
- Click Import note -> choose file(movielens.json).
- Check created "MovieLens analysis with Spark".
  
  
