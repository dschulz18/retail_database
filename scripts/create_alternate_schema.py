import psycopg2

conn_string = 'postgres://daniel@localhost/postgres'

with open('sql/alternate_schema.sql') as f:
  query = f.read()

# connect to postgres and execute sql commands
pg_conn = psycopg2.connect(conn_string)
cur = pg_conn.cursor()

cur.execute(query)

pg_conn.commit()
cur.close()
