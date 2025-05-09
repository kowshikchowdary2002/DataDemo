from pyspark.sql import SparkSession
#import mysql.connector

spark = SparkSession.builder.appName("FilterFailedTransactions").getOrCreate()

# Load cleaned file
df = spark.read.option("header", True).csv("gs://kowshikbank-bucket/cleaned/merged_transactions.csv")

# Filter failed transactions
df_failed = df.filter(df.transaction_status == "FAILED")

# Write to Cloud SQL (MySQL)
jdbc_url = "jdbc:mysql://34.30.9.217:3306/transaction_db"
properties = {
    "user": "trans-sql",
    "password": "trans-sql",
    "driver": "com.mysql.cj.jdbc.Driver"
}
df_failed.write.jdbc(url=jdbc_url, table="failed_transactions", mode="overwrite", properties=properties)


spark.stop()
