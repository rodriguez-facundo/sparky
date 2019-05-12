from __future__ import print_function

import sys
from random import random
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("PythonPi")\
        .getOrCreate()
    
    words = 'the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog'
    seq = words.split()
    print("HHOHOOHOHOHOHOHOHO")
    print("HHOHOOHOHOHOHOHOHO")
    print("HHOHOOHOHOHOHOHOHO")
    print("HHOHOOHOHOHOHOHOHO")
    data = spark.sparkContext.parallelize(seq)
    print("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAH")
    print("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAH")
    print("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAH")
    print("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAH")
    counts = data.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b).collect()
    print('HUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHGUHUHUHUHUHUHUHUHUHUHUHUHUHUHUH")
    print('HUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHGUHUHUHUHUHUHUHUHUHUHUHUHUHUHUH")
    print('HUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHGUHUHUHUHUHUHUHUHUHUHUHUHUHUHUH")
    print('HUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHUHGUHUHUHUHUHUHUHUHUHUHUHUHUHUHUH")
    print("This is the result of the operation:")
    dict(counts)
    sc.stop()

#     -------------------------

#     count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
#     print("Pi is roughly %f" % (4.0 * count / n))

#     spark.stop()
    
    
#     -------------------------

#     data = sc.parallelize(seq)
#     counts = data.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b).collect()
#     dict(counts)
#     sc.stop()
