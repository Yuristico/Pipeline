CREATE OR REPLACE VIEW total_transacciones_diarias AS
SELECT
    c.company_id,
    co.company_name,
    DATE(c.created_at) AS fecha,
    SUM(c.amount) AS monto_total
FROM
    charges c
JOIN
    companies co ON c.company_id = co.company_id
WHERE
    c.created_at IS NOT NULL
GROUP BY
    c.company_id,
    co.company_name,
    DATE(c.created_at)
ORDER BY
    fecha, company_name;
