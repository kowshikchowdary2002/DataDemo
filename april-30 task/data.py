from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("WriteToMySQL").getOrCreate()
# Sample data
data = [("John", 100), ("Jane", 200)]
df = spark.createDataFrame(data, ["name", "amount"])
# MySQL config
jdbc_url = "jdbc:mysql://34.132.173.149:3306/spark_output"
properties = {
 "user": "spark-user",
 "password": "spark-user",
 "driver": "com.mysql.cj.jdbc.Driver"
}
# Write to MySQL
df.write.jdbc(url=jdbc_url, table="transactions", mode="overwrite", properties=properties)
spark.stop()