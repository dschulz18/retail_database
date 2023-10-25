# Online Retail II Data Analysis Solution

## Overview
This document outlines a solution for analyzing the "Online Retail II" dataset, which includes data related to online retail sales. The solution involves setting up a database using PostgreSQL, importing the dataset into the database, and using PySparkSQL to perform data analysis to answer the specific business questions:

``````
• What are the top selling products?
• What is the revenue by product?
• What is the revenue per customer?
• What are the sales trends?
``````

## Requirements
This projects requires Python, PostgresSQL, and Spark. If using MacOS, you can install them using [Homebrew](https://brew.sh/).

### Python
```bash
brew install python
```

### PostgreSQL
```bash
brew install postgresql@14
```

To start and stop the service:
```bash
brew services start postgresql@14
brew services stop postgresql@14
```

### Spark
```bash
brew install apache-spark
```

Since we are connecting to the `PostgreSQL` database, we will also need to download the [JDBC driver](https://jdbc.postgresql.org/download/).

### Python Packages
You will also need the Python packages found in the requirements.txt file.
```bash
python3 -m pip install -r requirements.txt
```

## Data Ingestion
The script for ingesting the data is `scripts/data_ingestion.py`.

It downloads the data from `https://archive.ics.uci.edu/static/public/502/online+retail+ii.zip`, unzips it
then uses `pandas` to clean it, and store it as a CSV file.

The CSV file is loaded into `PostgresSQL` using `psycopg2`.

You will need to modify the PostgreSQL user to your own user, and set the path to the JDBC driver downloaded in the `Requirements` section.

```python
conn_string = 'postgres://{user}@localhost/postgres'
```

```python
spark = SparkSession.builder \
    .appName("PostgreSQL Connection with PySpark") \
    .config("spark.jars", "{JDBC-driver-path}") \
    .getOrCreate()
```

## Database Design
The desgin for what a schema might look like for a retail organisation is found in `sql/alternate_schema.sql`.
This is not the schema used for analysis, but can be loaded using the `scripts/create_alternate_schema.py` file. You will need to modify the PostgreSQL user to your own user.

```python
conn_string = 'postgres://{user}@localhost/postgres'
```


## Data Processing
I use PySparkSQL to process the data in Spark to answer the business questions.
The results are stored in the `results/` directory as either `tables/` or `plots/`. Plots are also displayed using `plotly`.

Both of these options can be turned on or off by editing the following lines:
```python
WRITE = True
DISPLAY = True
```

You will need to modify the PostgreSQL user to your own.

```python
properties = {
    "user": "{user}",
    # "password": "password",
    "driver": "org.postgresql.Driver"
}
```
