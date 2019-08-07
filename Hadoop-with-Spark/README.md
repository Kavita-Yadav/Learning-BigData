
###########################
#### Hadoop with Spark ####
###########################

- It is scalable.
- Fast & general engine for large scale data processing.
- It's fast. run program 100 times faster than Hadoop MapReduce in memory or 10 times faster on disk.
- DAG Engine(directed acyclic graph) ptimize workflows.
- Code in Python, Java or Scala.
- Resilient Distributed Dataset(RDD).

**Component of spark**
- Spark Streaming
- Spark SQL
- ML Lib
- GraphX

**The SparkContext**
- cerated by your driver program(main for spark).
- Is responsible for making RDD's resilient and distributed!
- Creates RDD's
- The Spark shell creates a "sc" object for you.

**Creating RDD's**
- nums = parallelize([1,2,3,4])
- sc.textFile("file:///c:/users/frank/gobs-o-text.txt")
        - or s3n:// , hdfs:// (It will return lined up input text from RDD)
- hiveCtx = HiveContext(sc) rows = hiveCtx.sql("SELECT name,age FROM users")
- Can also create from: JDBC, Cassandra, HBase, Elasticsearch, JSON, CSV, squence files, object files, various compressed formats.

**RDD's**
-RDD methods accept function as parameter.

**RDD Actions**
  Nothing actually happens in your driver program until an action is called!
- collect
- countByValue
- top
- count
- take
- reduce, etc.

**Tranforming RDD's**
- map, flatmap, filter, distinct, sample, union, intersection, subtract, cartesian.

**How to run python code in spark?**
1. Login to hadoop virtual machine using 'ssh maria_dev@127.0.0.1 -p 2222'.
2. Spark-submit name_of_python_file. eg: spark-submit WorstMovie.py.

**Dataset and Spark 2.0**

1. Working with structured data

        - Extends RDD to a "DataFrame" object
        - DataFrames: Contain Row objects, Can run SQL queries, Has a schema(leading to more efficient storage), Read and write 
                      a JSON,Hive, parquet, Read and write to JSON, Hive, parquet, Communicates with JDBC/ODBC, Tableau.
                      
2. Using SparkSQL in Python

        - from pyspark.sql import SQLContext, Row
        - hiveContext = HiveContext(sc)
        - inputData = spark,read.json(dataFile)
        - inputData.cerateOrReplaceTempView("myStructuredStuff")
        - myResultDataFrame = hiveContext.sql("""SELECT foo FROM bar ORDER BY foobar""")
3. More things that can do with dataframes

        - myResultDataFrame.show()
        - myResultDataFrame,select("someFieldName")
        - myResultDataFrame.filter(myResultDataFrame("someFieldName" > 200)
        - myResultDataFrame.groupBy(myResultDataFrame("someFieldName")).mean()
        - myResultDataFrame.rdd().map(mapperFunction)
        
4. Datasets

        - In Spark 2.0, a DataFrame is really a DataSet of Row objects.
        - DataSets can wrap known, typed data too. But this is mostly transparent to you in Python, since Python is 
          dynamically typed.
        - Spark 2.0 way is to use DataSets instead of DataFrames.

5. Shell access

        - Spark SQL exposes a JDBC/ODBC server( if you bbuilt Spark with Hive support).
        - Start it with sbin/star5t-thriftserver.sh
        - Listens on port 10000 by default
        - Connect using bin/beeline -u jdbc:hive2://localhost:10000
        - Viola, you have a SQL shell to Spark SQL
        - You can create new tables, or query existing ones that were cached using hiveCtx.cacheTable("tableName")
     
 6. User-defined functions (UDF's)
 
        - from pyspark.sql.types import IntegerType
        - hiveCtx.registerFunction("square", lambda x:x*x, IntegerType())
        - df = hiveCtx.sql("SELECT square('someNumericFiled') FROM tableName) 
        
        
