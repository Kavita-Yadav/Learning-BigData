##############################
#### PROGRAMMING HADOOP WITH PIG
##############################

**Introduction of Pig**

- Writing big code for mapper and reducer is taking lot of time. Pig introduces _iPigLatini_, a scripting language that lets you use SQL-like syntax to define your map and reduce steps. And highly extensible with user-defined functions(UDF's).
- There are different ways of running Pig scripts using command line interpreter Grunt,save a Pig script to file and run that from the commandline using 'Pig file_name', also there is Ambari view for Pig that write, run, save and load Pig scripts.

**Let's understand it with example,find oldest 5-star movie using Pig**

- JOIN

      DESCRIBE fievStarMovies;
      Describe nameLookup;
      fiveStarsWithData = JOIN fiveStarMovies BY movieID, nameLookup BY movieID;
      DESCRIBE fiveStarsWithData;
      DUMP fiveStarsWithData;

- ORDER BY

      oldestFiveStarMovies = ORDER fiveStarWithData BY nameLookup::releaseTime;
      DUMP oldestFiveStarMovies;
      
 - PIGSTORAGE
      
      Use PigStorage if you need a different delimeter.
      
       metadata = LOAD '/user/maria_dev/ml-10k/u.item'
                  USING PigStorage ('|') 
                  AS (movieID:int, movieTitle: chararray, releaseDate:chararray, videoRelease: chararray, imbdlink:chararray);
          
 - FOREACH/GENERATE
     
     Creating a realtion from another realtion.
      
       nameLookup = FOREACH metadata GENERATE movieID, movieTitle,
                    ToUnixTime(ToDate(releaseDte, 'dd-MMM-yyyy')) AS releaseTime;
                    
 - GROUP BY
          
        ratingsByMovie = GROUP ratings BY movieID;
        
 - FILTER
 
       fiveStarMovie = FILTER avgRatings BY avgRating > 4.0;
                  
      
**How to run Pig script on Ambari ?**
1. Go to http://127.0.0.1:8080/ .
2. Login with uname: maria_dev and pwd: maria_dev.
3. Go to Files View -> users -> maria_dev -> ml-100k (Note: Create folder ml-100k using 'New Folder' button, if folder not present).
4. Upload u.data and u.item file from movielens data folder.
5. Go to 'Pig View'.
6. Create 'New Script'. Name: OldButGold.
7. Copy content of 'Old5RatedMovieUsingPig.txt' file and paste into script window at Ambari.
8. Click on Execute and wait for the results.

_Note: For more faster result need to check 'execute on Tez' checkbox and click on 'Execute'._

**Pig Latin: Things you can do to a realtion**
- LOAD, STORE, DUMP
- FILTER, DISTINCT, FOREACH/GENERATE, MAPREDUCE, STREAM, SAMPLE
- JOIN, COGROUP, GROUP, CROSS, CUBE
- ORDER, RANK, LIMIT
- UNION, SPLIT

**Diagnostics**
- DESCRIBE, EXPLAIN, ILLUSTRATE

**User Defined Function**
- REGISTER, DEFINE, IMPORT

**Some Other Functions & Loaders**
- AVG, CONCAT, COUNT, MAX, MIN, SIZE, SUM
- PigStorage
- TextLoader
- JsonLoader
- AvroStorage
- ParquetLoader
- OrcStorage
- HBaseStorage

