from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def main():
    spark = SparkSession.builder \
        .appName("Customer Data Processing") \
        .getOrCreate()

    # Load the data
    df = spark.read.csv("data/raw/customers-1000.csv", header=True, inferSchema=True)

    # Remove duplicates and empty values
    df = df.dropDuplicates()
    df = df.na.drop()

    # Rename the first column to "target"
    first_column = df.columns[0]
    df = df.withColumnRenamed(first_column, "target")

    # Save the processed data
    df.write.mode("overwrite").parquet("data/processed/processed_data.parquet")

    # Split the data into training and testing datasets
    train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)
    train_df.write.mode("overwrite").parquet("data/processed/train_data.parquet")
    test_df.write.mode("overwrite").parquet("data/processed/test_data.parquet")

    spark.stop()

if __name__ == "__main__":
    main()