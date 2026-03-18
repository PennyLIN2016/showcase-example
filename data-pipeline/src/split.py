from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql.functions import col
from sklearn.model_selection import train_test_split

def split_data(df: DataFrame, test_size: float = 0.2) -> (DataFrame, DataFrame):
    """
    Splits the DataFrame into training and testing datasets.

    Parameters:
    df (DataFrame): The input DataFrame to split.
    test_size (float): The proportion of the dataset to include in the test split.

    Returns:
    DataFrame: Training dataset.
    DataFrame: Testing dataset.
    """
    train_df, test_df = train_test_split(df.toPandas(), test_size=test_size, random_state=42)
    return spark.createDataFrame(train_df), spark.createDataFrame(test_df)

def save_datasets(train_df: DataFrame, test_df: DataFrame, output_dir: str):
    """
    Saves the training and testing datasets to the specified directory.

    Parameters:
    train_df (DataFrame): The training dataset to save.
    test_df (DataFrame): The testing dataset to save.
    output_dir (str): The directory where datasets will be saved.
    """
    train_df.write.csv(f"{output_dir}/train.csv", header=True, mode='overwrite')
    test_df.write.csv(f"{output_dir}/test.csv", header=True, mode='overwrite')

if __name__ == "__main__":
    spark = SparkSession.builder.appName("DataSplitter").getOrCreate()
    # Assuming df is the DataFrame obtained from the preprocessing step
    output_directory = "data/processed"
    train_data, test_data = split_data(df)
    save_datasets(train_data, test_data, output_directory)