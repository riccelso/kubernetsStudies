from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession


conf = (
    SparkConf()\
    .set('spark.kubernetes.authenticate.driver.serviceAccountName', 'spark')
)
sc = SparkContext(conf=conf).getOrCreate()

spark = SparkSession.builder.appName('spark-k8s').getOrCreate()

# spark = SparkSession().builder.appName('spark-kubernets').getOrCreate()
spark.sparkContext.setLogLevel('INFO')

df = spark.range(1, 100)

df = df.withColumnRenamed(df.columns[0], 'MyRangeColumn')

df.show()
df.printSchema()

spark.stop()