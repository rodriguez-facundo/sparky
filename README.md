# sparky

How to ⚡️ :

1. `kubectl -n sparky get pods`
```
NAME                            READY     STATUS    RESTARTS   AGE
spark-master-7fc9767b48-4bqvj   1/1       Running   0          1m    <<<<<<<<<<< This ☝️ 
spark-worker-756d5f4d84-hvtck   1/1       Running   0          1m
spark-worker-756d5f4d84-wzgcv   1/1       Running   0          1m
```
2. kubectl -n sparky exec -it spark-master-7fc9767b48-4bqvj pyspark
```
Python 2.7.9 (default, Jun 29 2016, 13:08:31) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
19/05/08 20:15:56 WARN ObjectStore: Version information not found in metastore. hive.metastore.schema.verification is not enabled so recording the schema version 1.2.0
19/05/08 20:15:57 WARN ObjectStore: Failed to get database default, returning NoSuchObjectException
19/05/08 20:15:57 WARN ObjectStore: Failed to get database global_temp, returning NoSuchObjectException
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.2.1
      /_/

Using Python version 2.7.9 (default, Jun 29 2016 13:08:31)
SparkSession available as 'spark'.
>>>                                                                       <<<<<< We wait for this signal
```
3. Run:
```
words = 'the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog'
sc = SparkContext()
seq = words.split()
data = sc.parallelize(seq)
counts = data.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b).collect()
dict(counts)
sc.stop()
```
4. Wait for the answer that should be:

`{'brown': 2, 'lazy': 2, 'over': 2, 'fox': 2, 'dog': 2, 'quick': 2, 'the': 4, 'jumps': 2}`



----- 

Check the UI:

