WITH top_sellers AS (

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

)

SELECT
    description,
    DATE_PART('year', invoicedate) AS year,
    SUM(quantity) AS quantity_sold
FROM
    retail
WHERE description IN (SELECT description FROM top_sellers)
GROUP BY
    description,
    year
ORDER BY
    description,
    year
;
