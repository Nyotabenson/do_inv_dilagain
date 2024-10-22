USE do_inventory_db;

SELECT 
    outdate, Orders
FROM
    do_outbound
WHERE
    MONTH(outdate) = MONTH(CURDATE())
        AND YEAR(outdate) = YEAR(CURDATE());
