#########################
#### Spark Streaming ####
#########################

Process continous stream of data in near real-time

#### Why Spark Streaming?

- "Big data", if that never stops!
  For Example, data flowing in from user activity that's being captured in your web server logs that's just going to keep 
  coming in 24/7. In that case, you don't want to processing data on a batch basis, because batch gets too big too handle then 
  you can actually process your data in real time as it comes.
- Analyze data streams in real time, instead of in huge batch jobs daily.
- Analyzing streams of web log data to react to user behaviour.
- Analyze streams of real-time sensor data for "Internet of Things" stuff.

#### Spark Streaming: High Level

              |         |         |
              |         |         |       Data Streams
             \|/       \|/       \|/
            ________________________
           |        Receivers       |
            ________________________
                      _____
                     | RDD |
                      _____
                      _____               Batches of data
                     | RDD |              For a given time increment
                      _____
                      _____
                     | RDD |
                      _____
                      
              |         |         |
              |         |         |       Tranform & output to other systems   
             \|/       \|/       \|/
                    
 As you can see, bunch of data steaming coming in. Suppose that's coming from kafka or flume and listening to sockets on
 a TCP connection. But spark cluster have bunch of receivers that recieve data and spread it into little chunks. So you can
 give it a batch increment time of one second or two second or whatever appropriate and it will split that data in little
 one seconds increment or whatever given time increment in the individual RDD. SO each RDD withtin that stream of data will
 contain some discretized chunk of data recieved over some small time period. And there you can transform that data and process
 it like any other stream RDD or an outstream RDD. So it's not really real time because in real it's dealing with micro batches
 called RDD, those managed togethet as part of larger structure. So technically it's not real time, it's breaking dtaa into one
 second chunks. Processing of these chunks can happen in parallel across different worker nodes across spark cluster.

#### Dtreams (Discretized Streams)

              |         |         |
              |         |         |      
             \|/       \|/       \|/
            ________________________
           |        Receivers       |
            ________________________
                      _____      ___
                     | RDD |    | D |
                      _____     | S |
                      _____     | t |        
                     | RDD |    | r |        
                      _____     | e |
                      _____     | a |
                     | RDD |    | m |
                      _____      ___
                      
              |         |         |
              |         |         |       
             \|/       \|/       \|/
             
- Generates the RDD's for each time step, and can produce output at each time step.
- Can be transformed and acted on in much the same way as RDD's.
- Or you can access their underlying RDD's if you need them.

- _Stateless transformations on DStreams_
        - Map
        - Flatmap
        - Filter
        - reduceByKey
        
- _Stateful data_

        - You can also maintain a long-lived state on a Dstream
        - For example - running totals, broken down by keys
        - Another example: aggregating session data in web activity
        
- #### Windowed Transformations

        - Allow you to compute results across a loner time perios than your batch interval
        - Example: want to see top-sellers from the past hour by looking at activity data that's coming from your e-commerce 
          web-site from bunch of different sever.
          - You might process data every one second(the batch inteval)
          - But maintain a window of one hour
        - The window "slides" as time goes on, to represent batches within the window interval
        
  _Batch interval vs Slide interval vs Window interval_
  
      - The batch interval is how often data is captured into a DStream
      - The slide interval is how often a windowed transformation is computed
      - The window interval is how far back in time the windowed transformation goes
    
  _Example:_
    - Each batch contains one second of data(the batch interval)
    - We set up a window interal of 3 seconds and a slide interval of 2 seconds.
    
          Time ----------------------------------------------->
        
          Batch     Batch     Batch     Batch     Batch     Batch
            \       /   \       |       /   \         |       /
              \    /      \_____|     /       \_______|     /
              Compute          Compute               Compute
              result            result               result
              
 _Windowed transformations: code_
 
      - The batch interval is set up with your SparkContext:
            scc = StreamingContext(sc, 1)
      - You can use reduceByWindow() or reduceByKeyAndWindow() to aggregate data across a longer period of time!
            hashtagCounts = hashtagKeyValues.reduceByKeyAndWindow(lambda x, y:x + y, lambda x,y : x-y, 300, 1)
            
#### What is structured streaming ?
    - A new, higher-level API for streaming strcutured data
        - Available in Spark 2.0 and 2.1 as an experimental release.
    - Uses DataSetsta
        - Like a DataFrame, but with more explicit type information.
        - A DataFrame is really a DataSet[Row]
        - Imagine a DataFrame that never ends:
            - New data just keeps getting appended to it
            - Your continous application keeps querying updated data as it comes in
              
                    Data stream                 Unbounded Table
                                               _________________
               - - - - - -------->            |     |     |     |
                |  |  |                        _________________
                |  |  |                       |     |     |     |   
                |  |  |                        _________________
                |  |  |                       |     |     |     |   new data in stream
                |  |  |                        _________________
                |  |  |                                                     =
                |  |  |                                             
                |  |  |                        _________________
                |  |   -------------------->  |     |     |     |    new rows appened to 
                |  |                           _________________      input table
                |  |                            
                |  |                           _________________
                |   ------------------------> |     |     |     |
                |                              _________________
                |                               
                |                              _________________
                 ---------------------------> |     |     |     |
                                               _________________
                                               
                              Data stream as an unbounded Input Table
                              
 _Advantages of Structured Streaming_
 
 - Streaming code looks a lot like the equivalend non- streaming code
 - Structured data allows Spark to represent data more efficiently
 - SQL-style queries allow for query optimization opportunities- and even better performance.
 - Interoperability with other Spark components based on DataSets.
    - MLLib is also moving toward DataSets as its primary API.
 - DataSets in general is the direction Spark is moving.
 - Once you have a SparkSession, you can stream data, query it, and write out the results.
      - 2 lines of code to stream in structured JSON log data, count up "action" values for each hour, and write out the             results.
      
            val inputDF = spark.readStream.json("s3://logs")
            inputDF.gorupBy($"action", window($"time", "1 hour")).count()
                .writeStream.format("jdbc").start("jdbc:mysql//...")
            
 #### Spark Streaming with Flume
 
 - We'll set up Flume to use a spooldir source as before
 - But use an Avro sink to connect it to our Spark Streaming job!
    - Use a window to aggregate how often each unique URL sppears from our access log.
 - Using Avro in this manner is a "push" mechanism to Spark Streaming
    - You can also "pull" data by using a custom sink for Spark Streaming
   
                           -------------------------------------------------- 
                          |                        Flume                     |  
           ________       |  ___________           __________        ______  |                      _________
          |  Logs  | ---> | | Source    |  --->   | Channel  | ---> | Sink | |---> Spark      ---> | Console |
           ________       | |(spooldir) |         | (memory) |      |(Avro)| |     Streaming        _________
                          |  ___________           __________        ______  |
                          |                                                  |
                           --------------------------------------------------
_Analyze web logs published with Flume using Spark Streaming_

- Login to hadoop terminal as maria_dev
- wget http://media.sundog-soft.com/hadoop/sparkstreaminglume.conf
- wget http://media.sundog-soft.com/hadoop/SparkFlume.py
- 
- 
