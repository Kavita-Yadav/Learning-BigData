#########################
####Hadoop with Spark####
#########################

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
2. Spark-submit name_of_python_file. eg: spark-submit WorstMovie.py .
