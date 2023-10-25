SELECT
    DATE_PART('year', invoicedate) AS year,
    DATE_PART('month', invoicedate)  AS month,
    SUM(price * quantity) AS revenue
FROM
    retail
GROUP BY
    year,
    month
ORDER BY
    year,
    month
;
