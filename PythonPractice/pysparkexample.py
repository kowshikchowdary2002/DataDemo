# sample_app.py
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Sample").getOrCreate()

data = [("John", 28), ("Jane", 35), ("Doe", 40)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()

df.createOrReplaceTempView("people")
spark.sql("SELECT * FROM people WHERE Age > 30").show()

spark.stop()
