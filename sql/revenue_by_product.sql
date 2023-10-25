SELECT
    description AS product,
    SUM(price * quantity) AS total_revenue
FROM
    retail
GROUP BY
    product
ORDER BY
    total_revenue DESC
LIMIT 20
;
