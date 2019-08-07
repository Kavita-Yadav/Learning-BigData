#####PROGRAMMING HADOOP WITH PIG#####

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
                  
      
