#Count how many times each movie was rated in a dataset

from mrjob.job import MRJob
from mrjob.step import MRStep
class RatingsBreakdown (MRJob):
      def steps(self):
          return[
                MRStep(mapper = self.mapper_get_ratings,
                reducer = self.reducer_count_ratings)
          ]

       #Mapper function
       def mapper_get_ratings(self, _ , line):
           (userID, movieID, rating, timestamp) = line.split('\t') 
            yield movieID,1

        #Reducer function
        def reducer_count_ratings(self,key,values):
            yield key, sum(values)

if __name__ == '__main__':
RatingBreakdown.run()
