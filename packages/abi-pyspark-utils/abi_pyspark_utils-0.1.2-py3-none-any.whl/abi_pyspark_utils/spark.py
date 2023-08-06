from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    # General
    .master('local[*]')
    .config("spark.driver.memory", "50g")
    .config("spark.driver.maxResultSize", 0)

    # PyArrow for dtypes conversions
    .config("spark.sql.execution.arrow.pyspark.enabled", "true")

    # Jars compatible with the base-notebook image (Python 3.8.8, PySpark 3.1.1)
    .config('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.1.1,io.delta:delta-core_2.12:1.0.1')

    # Delta Lake setup
    # Set spark.hadoop.fs.s3a.access/secret.key if not using env vars
    .config("spark.hadoop.fs.s3a.connection.maximum", 128)
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .config("spark.delta.logStore.class", "org.apache.spark.sql.delta.storage.S3SingleDriverLogStore")
    .getOrCreate()
)
