from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, udf
from pyspark.sql.types import StringType


def initialize_spark():
    """Initialize and return a Spark session."""
    return SparkSession.builder.appName("Spark SQL").getOrCreate()


def read_text_file(spark, file_path):
    """Read a text file into a DataFrame."""
    return spark.read.text(file_path)


def extract_digits(value):
    """UDF to extract digits from a string."""
    return "".join(filter(str.isdigit, str(value)))


def calibrate_digits(digits):
    """UDF to calibrate digits by concatenating the first and last digit."""
    return digits[0] + digits[-1:]


def main():
    spark = initialize_spark()

    df = read_text_file(
        spark,
        "/workspaces/being-data-engineer/apache-spark"
        "/advent_of_code/2023/1/input.txt",
    )

    digits_udf = udf(extract_digits, StringType())
    calibration_udf = udf(calibrate_digits, StringType())

    digits_only = df.withColumn("digits_only", digits_udf(col("value"))).filter(
        col("digits_only").isNotNull()
    )
    calibration_value = digits_only.withColumn(
        "calibration_value", calibration_udf(col("digits_only"))
    )

    digits_only.show()
    calibration_value.show()

    calibration_values_sum = calibration_value.agg(sum("calibration_value")).collect()[
        0
    ][0]
    print(f"Sum of calibration values: {calibration_values_sum}")

    spark.stop()


if __name__ == "__main__":
    main()
