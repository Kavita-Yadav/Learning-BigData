# Learning-BigData-Hadoop

######################################
##### Environment Setup for Hadoop #####
######################################

- Installation of Virtual machine:
1. Go to https://www.virtualbox.org and download a version for your OS.(I have installed for Ubuntu)
2. After download, run the .exe file and install the virtual box on your machine.

- Download image for Hadoop:
1. Go to https://www.cloudera.com/downloads.html and Click on Download Hortronworks Sandbox link.
2. Click on Download Hortronworks HDP 'Download Now' button.
3. Choose installation type as "Virtual Box" in Get Started Now section and click on 'Let's Go' button.
4. Fill up the details and click on 'Continue' and then 'Submit' Button.
5. Download the 2.5.0 version of Sandbox HDP Virtualbox Downloads.
6. Open downloaded .ova file
8. Click on 'Import'.
9. Click on 'Start' to start the machine.

- Web UI for Hadoop Ambari:
1. Go to http://127.0.0.1:8888/ .
2. Click on 'Please Disable Popup Blocker'
3. Sign in with username: maria_dev and password: maria_dev
4. To reset password for user 'admin':
        - su root
        - ambari-admin-password-reset

- Data preparation:
1. You can get the data directly from here: https://github.com/Kavita-Yadav/Learning-Hadoop-and-bigData/tree/master/MovieLensData.
2. It has detailed description of data from grouplens.

        OR
        
1. Go to https://grouplens.org/ or (Direct link for 100k dataset: https://grouplens.org/datasets/movielens/100k/).
2. Download MovieLens 100k Dataset by downloading 'ml-100k.zip' data file.
3. Unzip 'ml-100k.zip'.
4. You can also try this with 1M, 10M and 20M data from here https://grouplens.org/datasets/movielens/.

      
