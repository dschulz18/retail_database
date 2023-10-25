SELECT
    country,
    DATE_PART('year', invoicedate) AS year,
    SUM(quantity * price) AS revenue
FROM
    retail
GROUP BY
    country,
    year
ORDER BY
    country,
    year
;
