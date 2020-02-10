#############
#### HUE ####
#############

Hadoop User Experience

#### A tale of two distros
- Hortronworks:
    - Ambari used for management and query/files UI.
    - Zeppelin used for notebook.
- Cloudera
    - Hue used for query/files UI and notebook.
    - Cloudera Manager used for management.
- Hue is Cloudera's Ambari - sort of.
- It has a builtin Oozie editor, just like Oozie you can create workflows in it using graphical editor instead of writing XML
  files. So it is much more easier than Oozie.
- Just like Ambari, it also offers interfaces to other systems like Pig, Hive, HDFS, Sqoop.
- It also offers a view into HBase and Spark where you can issue your queries thorough UI.
- Spark interface is kind of like the Zepppelin notebook and notebooks are built-in as part of Hue.
- It is open source.

#### Working on Hue
- Go to gethue.com .
- Click on Try it now. Sign in using uname: demo and pwd: demo
- And you can expolre the various examples in the HUE.
