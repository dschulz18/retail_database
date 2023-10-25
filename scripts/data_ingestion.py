import io
import os
import pandas as pd
import psycopg2
import requests
from zipfile import ZipFile

RAW_PATH = 'data/raw/online+retail+ii.zip'
PROCESSED_PATH = 'data/processed/clean.csv'
SCHEMA_QUERY_PATH = 'sql/schema.sql'
COPY_QUERY_PATH = 'sql/copy_data.sql'

REFRESH_RAW=False
REFRESH_PROCESSED=False


# Download dataset
if not os.path.exists(RAW_PATH) or REFRESH_RAW:
    # Define the URL of the dataset
    url = "https://archive.ics.uci.edu/static/public/502/online+retail+ii.zip"

    # Download the dataset from the URL
    if not os.path.exists(RAW_PATH):
        response = requests.get(url)
        with open(RAW_PATH, "wb") as file:
            file.write(response.content)

# Clean dataset
if not os.path.exists(PROCESSED_PATH) or REFRESH_PROCESSED:
    # zip file handler
    zip = ZipFile(RAW_PATH)

    # read into pandas
    df = pd.concat(pd.read_excel(io.BytesIO(zip.read(zip.namelist()[0])), sheet_name=None))

    # save cleaned dataset as csv
    df.drop_duplicates(inplace=True)
    df.drop(df[(df['Customer ID'].isna()) & (df['Quantity'] < 0)].index, inplace=True)
    df.dropna(subset=['Description'])
    df.to_csv(PROCESSED_PATH, index=False)

# postgres connection string
conn_string = 'postgres://daniel@localhost/postgres'

# connect to postgres and execute sql commands
pg_conn = psycopg2.connect(conn_string)
cur = pg_conn.cursor()

# create retail table
with open(SCHEMA_QUERY_PATH) as f:
    cur.execute('DROP TABLE IF EXISTS retail')
    cur.execute(f.read())

# copy data
with open(COPY_QUERY_PATH) as f:
    cur.execute(f.read())

# commit transaction and close connection
pg_conn.commit()
cur.close()
