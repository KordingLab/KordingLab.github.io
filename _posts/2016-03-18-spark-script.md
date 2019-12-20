---
title: Example how to run PySpark
description: small snippet to run PySpark snippet
categories: blog
header-img: images/post/dino.jpg
---

In this post, we'll describe how to download and run Spark.

### Download Spark

Basically, here is Spark [page](http://spark.apache.org/). You can go to download
[page](http://spark.apache.org/downloads.html) in order to download Spark.

- Choose Spark release: `1.6.0`
- Choose a package type: `Pre-built for Hadoop 2.6 or later`
- Choose a download type: `Direct Download`

Then click download Spark link, it will download Spark (size around 276 MB compressed).
If you want to download to instance, just copy the link and use `wget` to download.


### Run PySpark on IPython notebook

Assume we download Spark into Desktop directory. We first have to path to Spark environment path
into `.bash_profile`, something like the following line

```bash
export SPARK_HOME=~/Desktop/spark-1.6.0-bin-hadoop2.6
```

Simple way to run `pyspark` shell is running `.bin/pyspark` (if you are in `spark-1.6.0-bin-hadoop2.6` folder).
However, we typically run `pyspark` on IPython notebook. And it will look something like

```bash
IPYTHON_OPTS="notebook" ~/Desktop/spark-1.6.0-bin-hadoop2.6/bin/pyspark
```

You can also customize Spark script as follows where we state how many cores we want to use in `--master local[4]`,
driver memory and executor-memory in `--driver-memory, --executor-memory`. Also the output size is now set to `spark.driver.maxResultSize=0` which means output can be any size. You can also set it to `1g` for maximum 1 Gb output size

```bash
IPYTHON_OPTS="notebook --ip=* --no-browser" ~/spark-1.6.0-bin-hadoop2.6/bin/pyspark --master local[4] --driver-memory 32g --executor-memory 32g --conf spark.driver.maxResultSize=0
```

### Snippet

Now, we're going to run small example snippet in case you're submitting the job on cluster.
First, we can create python file name `spark_example.py`.

```python
import os
from pyspark import SparkConf, SparkContext

# Configure the environment                                                     
if 'SPARK_HOME' not in os.environ:
    os.environ['SPARK_HOME'] = '/home/ubuntu/spark-1.6.0-bin-hadoop2.6'

conf = SparkConf().setAppName('pubmed_open_access').setMaster('local[32]')
sc = SparkContext(conf=conf)

if __name__ == '__main__':
    ls = range(100)
    ls_rdd = sc.parallelize(ls, numSlices=1000)
    ls_out = ls_rdd.map(lambda x: x+1).collect()
    print 'output!: ', ls_out
```

Here is the bash script to run the code above.

```bash
~/spark-1.6.0-bin-hadoop2.6/bin/pyspark --master local[8] --driver-memory 12g --executor-memory 12g spark_example.py
```
