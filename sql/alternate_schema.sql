CREATE TABLE IF NOT EXISTS customers (
  customer_id             SERIAL PRIMARY KEY,
  country                 VARCHAR(50)
);


CREATE TABLE IF NOT EXISTS products (
  stockcode               VARCHAR(20) PRIMARY KEY,
  description             TEXT,
  price                   NUMERIC(10,2)
);


CREATE TABLE IF NOT EXISTS orders (
  invoice                  SERIAL PRIMARY KEY,
  invoicedate              TIMESTAMP,
  customer_id              INT REFERENCES customers(customer_id)
);


CREATE TABLE IF NOT EXISTS order_details (
  order_detail_id           SERIAL PRIMARY KEY,
  invoice                   INT REFERENCES orders(invoice),
  stockcode                 VARCHAR(20) REFERENCES products(stockcode),
  quantity                  NUMERIC(10,2),
  total_price               NUMERIC(10,2)
);

CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_orderdetails_order_id ON order_details(invoice);
CREATE INDEX idx_orderdetails_product_id ON order_details(stockcode);

ALTER TABLE customers ADD CONSTRAINT unique_customer_id UNIQUE (customer_id);
ALTER TABLE products ADD CONSTRAINT unique_product_id UNIQUE (stockcode);
ALTER TABLE order_details ADD CHECK (quantity >= 0);
