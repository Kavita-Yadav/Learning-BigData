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

        This data set consists of:
                * 100,000 ratings (1-5) from 943 users on 1682 movies. 
                * Each user has rated at least 20 movies. 
                * Simple demographic info for the users (age, gender, occupation, zip)


        - DETAILED DESCRIPTIONS OF DATA FILES:

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
| 1 | `user id` | unique identity number of users who gave the ratings to the movie |
| 2 | `item id` | unique identity number of movie/item which is rated by user |
| 3 | `rating` | number of rating given by user out of 5 star; 5 start means movie is super hit; 1 means movie is flop |
| 4 | `timestamp` | The time stamps are unix seconds since 1/1/1970 UTC |
                              
          - u.info   -- The number of users, items, and ratings in the u data set.      

| Attributes | Total Number |
| --- | --- |
| users | 943 |
| items | 1682 |
| ratings |  100000 |              

          - u.item  -- Information about the items (movies); 
                       this is a tab separated list of all fields belongs to this file:
 
| Column Index | Column Name | Description |
| --- | --- | --- |
| 0 | `movie id` | unique identity number of movie/item which is rated by user, it is similar to item id from u.data |
| 1 | `movie title` | The title of the movie |
| 2 | `release date` | The release date of the movie |
| 3 | `video release date` | This column is blank |
| 4 | `IMDb URL` | IMDb URL link of the movie |
| 5 | `unknown` | Movie belongs to **unknown** genre |
| 6 | `Action` | Movie belongs to **Action** genre |
| 7 | `Adventure` | Movie belongs to **Adventure** genre |
| 8 | `Animation` | Movie belongs to **Animation** genre |
| 9 | `Children's` | Movie belongs to **Children's** genre |
| 10 | `Comedy` | Movie belongs to **Comedy** genre |
| 11 | `Crime` | Movie belongs to **Crime** genre |
| 12 | `Documentary` | Movie belongs to **Documentary** genre |
| 13 | `Drama` | Movie belongs to **Drama** genre |
| 14 | `Fantasy` | Movie belongs to **Fantasy** genre |
| 15 | `Film-Noir` | Movie belongs to **Film-Noir** genre |
| 16 | `Horror` | Movie belongs to **Horror** genre |
| 17 | `Musical` | Movie belongs to **Musical** genre |
| 18 | `Mystery` | Movie belongs to **Mystery** genre |
| 19 | `Romance` | Movie belongs to **Romance** genre |
| 20 | `Sci-Fi` | Movie belongs to **Sci-Fi** genre |
| 21 | `Thriller` | Movie belongs to **Thriller** genre |
| 22 | `War` | Movie belongs to **War** genre |
| 23 | `Western` | Movie belongs to **Western** genre |

Note: The last 19 fields are the genres of the movies, a 1 indicates the movie is of that genre, a 0 indicates it is not; movies can be in several genres at once. The movie ids are the ones used in the u.data data set.
                              
          - u.genre  -- A list of the genres.
  
| Genre Name | Genre id|
| --- | --- |
| unknown | 0 |
| Action | 1 |
| Adventure | 2 |
| Animation | 3 |
| Children's | 4 |
| Comedy | 5 |
| Crime | 6 |
| Documentary | 7 |
| Drama | 8 |
| Fantasy | 9 |
| Film-Noir | 10 |
| Horror | 11 |
| Musical | 12 |
| Mystery | 13 |
| Romance | 14 |
| Sci-Fi | 15 |
| Thriller | 16 |
| War | 17 |
| Western | 18 |
 
         - u.user   -- Demographic information about the users; 
                       this is a tab separated list of users data fields:
                              
| Column Index | Column Name | Description |
| --- | --- | --- |
| 1 | `user id` | unique identity number of users who gave the ratings to the movie, it is similar to user id from u.data |
| 2 | `age` | Age of the users who rated the movies |
| 3 | `gender` | Gender of the users |
| 4 | `occupation` | Occupation of the users|
| 5 | `zip code` | Zip code of the location where users lives |

         - u.occupation -- A list of the occupations of the users who rated the movies.
 
|  List Of Occupation |
| --- |
| administrator, artist, doctor, educator, engineer, entertainment, executive, healthcare, homemaker, lawyer, librarian, marketing, none, other, programmer,retired, salesman ,scientist, student, technician, writer |

          - u1.base    -- The data sets u1.base and u1.test through u5.base and u5.test
            u1.test       are 80%/20% splits of the u data into training and test data.
            u2.base       Each of u1, ..., u5 have disjoint test sets; this if for
            u2.test       5 fold cross validation (where you repeat your experiment
            u3.base       with each training and test set and average the results).
            u3.test       These data sets can be generated from u.data by mku.sh.
            u4.base
            u4.test
            u5.base
            u5.test

          - ua.base    -- The data sets ua.base, ua.test, ub.base, and ub.test
            ua.test       split the u data into a training set and a test set with
            ub.base       exactly 10 ratings per user in the test set.  The sets
            ub.test       ua.test and ub.test are disjoint.  These data sets can
                                      be generated from u.data by mku.sh.

           - allbut.pl  -- The script that generates training and test sets where
                                      all but n of a users ratings are in the training data.

           - mku.sh     -- A shell script to generate all the u data sets from u.data.
