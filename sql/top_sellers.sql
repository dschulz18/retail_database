SELECT
    description,
    SUM(quantity) AS quantity_sold
FROM
    retail
GROUP BY
    description
ORDER BY
    quantity_sold DESC
LIMIT 20
;
