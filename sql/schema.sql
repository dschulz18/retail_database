CREATE TABLE IF NOT EXISTS retail (
  invoice                 VARCHAR(20),
  stockcode               VARCHAR(20),
  description             TEXT,
  quantity                NUMERIC(10,2),
  invoicedate             TIMESTAMP,
  price                   NUMERIC(10,2),
  customer_id             VARCHAR(20),
  country                 VARCHAR(50)
);
