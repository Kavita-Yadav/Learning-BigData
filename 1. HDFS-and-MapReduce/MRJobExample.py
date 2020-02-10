from mrjob.job import MRJob
from mrjob.step import MRStep
class RatingsBreakdown (MRJob):
      # To define multiple steps, override steps() to return a list of MRSteps.
      def steps(self):
          return[
                MRStep(mapper = self.mapper_get_ratings,
                reducer = self.reducer_count_ratings)
          ]

       #Mapper function syntax: def mapper(self, _ , line)
       def mapper_get_ratings(self, _ , line):
           (userID, movieID, rating, timestamp) = line.split('\t')
            # yield sends a value back to caller
            yield rating,1

        #Reducer function syntax: def reducer(self, key, values)
        def reducer_count_ratings(self,key,values):
            yield key, sum(values)

if __name__ == '__main__':
   # running main class
   RatingBreakdown.run()
