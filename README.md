# Learning-BigData-Hadoop

######################################
##### Environment Setup for Hadoop #####
######################################

- #Installation of Virtual machine:
1. Go to https://www.virtualbox.org and download a version for your OS.(I have installed for Ubuntu)
2. After download, run the .exe file and install the virtual box on your machine.

- #Download image for Hadoop:
1. Go to https://www.cloudera.com/downloads.html and Click on Download Hortronworks Sandbox link.
2. Click on Download Hortronworks HDP 'Download Now' button.
3. Choose installation type as "Virtual Box" in Get Started Now section and click on 'Let's Go' button.
4. Fill up the details and click on 'Continue' and then 'Submit' Button.
5. Download the 2.5.0 version of Sandbox HDP Virtualbox Downloads.
6. Open downloaded .ova file
8. Click on 'Import'.
9. Click on 'Start' to start the machine.

- #Web UI for Hadoop Ambari:
1. Go to http://127.0.0.1:8888/ .
2. Click on 'Please Disable Popup Blocker'
3. Sign in with username: maria_dev and password: maria_dev
4. To reset password for user 'admin':
        - su root
        - ambari-admin-password-reset

- #Data preparation:
1. Go to https://grouplens.org/ .
2. Download MovieLens 100k Dataset by downloading 'ml-100k.zip' data file.
3. Unzip 'ml-100k.zip'

-  DETAILED DESCRIPTIONS OF DATA FILES:
     
    - ml-data.tar.gz   -- Compressed tar file.  To rebuild the u data files do this:
                                gunzip ml-data.tar.gz
                                tar xvf ml-data.tar
                                mku.sh
    - u.data     -- The full u data set, 100000 ratings by 943 users on 1682 items.
                              Each user has rated at least 20 movies.  Users and items are
                              numbered consecutively from 1.  The data is randomly
                              ordered. This is a tab separated list of data inside a u.data file:                            

| Column Index | Column Name | Description |
| --- | --- | --- |
| 0 | `user id` | unique identity number of users who gave the ratings to the movie |
| 1 | `item id` | unique identity number of movie/item which is rated by user |
| 2 | `rating` | number of rating given by user out of 5 star; 5 start means movie is super hit; 1 means movie is flop |
| 3 | `timestamp` | The time stamps are unix seconds since 1/1/1970 UTC |
                              
   - u.info     -- The number of users, items, and ratings in the u data set.    
      
| Attributes| Total Number |
| --- | --- |
| users | 943 |
| items | 1682 |
| ratings |  100000 |
                              

                

                u.item     -- Information about the items (movies); this is a tab separated
                              list of
                              movie id | movie title | release date | video release date |
                              IMDb URL | unknown | Action | Adventure | Animation |
                              Children's | Comedy | Crime | Documentary | Drama | Fantasy |
                              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
                              Thriller | War | Western |
                              The last 19 fields are the genres, a 1 indicates the movie
                              is of that genre, a 0 indicates it is not; movies can be in
                              several genres at once.
                              The movie ids are the ones used in the u.data data set.

                u.genre    -- A list of the genres.

                u.user     -- Demographic information about the users; this is a tab
                              separated list of
                              user id | age | gender | occupation | zip code
                              The user ids are the ones used in the u.data data set.

                u.occupation -- A list of the occupations.

                u1.base    -- The data sets u1.base and u1.test through u5.base and u5.test
                u1.test       are 80%/20% splits of the u data into training and test data.
                u2.base       Each of u1, ..., u5 have disjoint test sets; this if for
                u2.test       5 fold cross validation (where you repeat your experiment
                u3.base       with each training and test set and average the results).
                u3.test       These data sets can be generated from u.data by mku.sh.
                u4.base
                u4.test
                u5.base
                u5.test

                ua.base    -- The data sets ua.base, ua.test, ub.base, and ub.test
                ua.test       split the u data into a training set and a test set with
                ub.base       exactly 10 ratings per user in the test set.  The sets
                ub.test       ua.test and ub.test are disjoint.  These data sets can
                              be generated from u.data by mku.sh.

                allbut.pl  -- The script that generates training and test sets where
                              all but n of a users ratings are in the training data.

                mku.sh     -- A shell script to generate all the u data sets from u.data.
