import findspark
import os
import pandas as pd
import plotly.express as px
from pyspark.sql import SparkSession

WRITE = True
DISPLAY = True

URL = "jdbc:postgresql://localhost:5432/postgres"
TABLE_NAME = 'retail'

# initialise spark
findspark.init()

spark = SparkSession.builder \
    .appName("PostgreSQL Connection with PySpark") \
    .config("spark.jars", "/usr/local/Cellar/apache-spark/3.5.0/libexec/jars/postgresql-42.6.0.jar") \
    .getOrCreate()

properties = {
    "user": "daniel",
    # "password": "password",
    "driver": "org.postgresql.Driver"
}

# connect to postgres via jdbc and create spark table
df = spark.read.jdbc(URL, TABLE_NAME, properties=properties)
df.createOrReplaceTempView("retail")

# table queries
table_query_paths = ['sql/top_sellers.sql', 'sql/revenue_by_product.sql', 'sql/revenue_by_customer.sql']

if WRITE:
    for path in table_query_paths:
        with open(path) as f:
            spark.sql(f.read()).toPandas().to_csv(f'results/tables/{os.path.basename(path)}.csv', index=False)

# plot queries
# revenue per month
with open('sql/revenue_by_month.sql') as f:
    query = f.read()

df = spark.sql(query).toPandas()
df['year_month'] = pd.to_datetime(df[['year', 'month']].assign(DAY=1))
fig = px.line(df, x="year_month", y="revenue", title='Revenue by month')

if WRITE:
    fig.write_image('results/plots/revenue_by_month.png')

if DISPLAY:
    fig.show()


# revenue per product
with open('sql/quantity_per_product.sql') as f:
    query = f.read()

df = spark.sql(query).toPandas()
df['year'] = df['year'].astype('category')
fig = px.bar(df, x="description", y="quantity_sold", color="year", barmode='group', title='Quantity per product per year')

if WRITE:
    fig.write_image('results/plots/quantity_per_product.png')

if DISPLAY:
    fig.show()


# quantity per country
with open('sql/quantity_per_country.sql') as f:
    query = f.read()

df = spark.sql(query).toPandas()
df['year'] = df['year'].astype('category')
fig = px.bar(df, x="country", y="revenue", color="year", barmode='group', title='Quantity per country per year')

if WRITE:
    fig.write_image("results/plots/quantity_per_country.png")

if DISPLAY:
    fig.show()
