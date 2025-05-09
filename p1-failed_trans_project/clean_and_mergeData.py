from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim

spark = SparkSession.builder.appName("CleanAndMergeTransactions").getOrCreate()

# Load all CSVs
df = spark.read.option("header", True).csv("gs://kowshikbank-bucket/transactions/*.csv")

# Drop rows with nulls or blank columns
df_clean = df.dropna(how='any')
df_clean = df_clean.filter(~(col('transaction_id') == "") & ~(col('transaction_status') == ""))

# Save to a single CSV file
df_clean.coalesce(1).write.option("header", True).csv("gs://kowshikbank-bucket/cleaned/merged_transactions.csv", mode='overwrite')

spark.stop()
