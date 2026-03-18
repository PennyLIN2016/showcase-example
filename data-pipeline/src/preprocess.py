from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def load_data(file_path):
    spark = SparkSession.builder.appName("DataPreprocessing").getOrCreate()
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    return df

def preprocess_data(df):
    df = df.dropDuplicates()
    df = df.na.drop()
    df = df.withColumnRenamed(df.columns[0], "target")
    return df

def save_processed_data(df, output_path):
    df.write.mode("overwrite").csv(output_path, header=True)

def main():
    input_path = "data/raw/customers-1000.csv"
    output_path = "data/processed/processed_customers.csv"
    
    df = load_data(input_path)
    processed_df = preprocess_data(df)
    save_processed_data(processed_df, output_path)

if __name__ == "__main__":
    main()