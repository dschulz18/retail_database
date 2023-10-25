SELECT
    customer_id,
    SUM(price * quantity) AS revenue
FROM
    retail
GROUP BY
    customer_id
ORDER BY
    revenue DESC
LIMIT 20
;
