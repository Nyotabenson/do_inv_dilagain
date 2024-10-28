USE do_inventory_db;

select * from do_outbound;


# updating a value
update do_outbound
set Orders = 291
where plastic_bags_small = 130 ;

#Fetching daily orders
SELECT 
    outdate, Orders
FROM
    do_outbound
WHERE
    MONTH(outdate) = MONTH(CURDATE())
        AND YEAR(outdate) = YEAR(CURDATE());


CREATE TABLE selling_price (
    Num int PRIMARY KEY,
    clear_tapes INT,
    branded_tapes INT,
    plastic_bags_small INT,
    carton_boxes_small INT,
    carton_boxes_medium INT,
    carton_boxes_large INT,
    plastic_bags_medium INT,
    kg_90_suck INT,
    kg_50_suck INT
);
INSERT INTO selling_price ( Num , clear_tapes, branded_tapes, plastic_bags_small, carton_boxes_small,
    carton_boxes_medium, carton_boxes_large, plastic_bags_medium, kg_90_suck, kg_50_suck)
 VALUES (1, 99, 220, 6, 20, 40, 72, 13, 33, 25);   
 
 DROP TABLE selling_price;
 
 SELECT 
    *
FROM
    selling_price;
 
 
 SELECT 
    SUM(clear_tapes) * (SELECT 
            clear_tapes
        FROM
            selling_price) + SUM(branded_tapes) * (SELECT 
            branded_tapes
        FROM
            selling_price) + SUM(plastic_bags_small) * (SELECT 
            plastic_bags_small
        FROM
            selling_price) + SUM(carton_boxes_small) * (SELECT 
            carton_boxes_small
        FROM
            selling_price) + SUM(carton_boxes_medium) * (SELECT 
            carton_boxes_medium
        FROM
            selling_price) + SUM(carton_boxes_large) * (SELECT 
            carton_boxes_large
        FROM
            selling_price) + SUM(plastic_bags_medium) * (SELECT 
            plastic_bags_medium
        FROM
            selling_price) + SUM(kg_90_suck) * (SELECT 
            kg_90_suck
        FROM
            selling_price) + SUM(kg_50_suck) * (SELECT 
            kg_50_suck
        FROM
            selling_price) AS total_sale
FROM
    do_outbound;
 
 select sum(clear_tapes) from do_outbound;
 
 CREATE TABLE buying_price (
    Num int PRIMARY KEY,
    clear_tapes INT,
    branded_tapes INT,
    plastic_bags_small INT,
    carton_boxes_small INT,
    carton_boxes_medium INT,
    carton_boxes_large INT,
    plastic_bags_medium INT,
    kg_90_suck INT,
    kg_50_suck INT
);
 
 INSERT INTO buying_price ( Num , clear_tapes, branded_tapes, plastic_bags_small, carton_boxes_small,
    carton_boxes_medium, carton_boxes_large, plastic_bags_medium, kg_90_suck, kg_50_suck)
 VALUES (1, 88, 200, 5, 18, 36, 66, 12, 24, 18);  
 
  CREATE TABLE profit (
    Num int PRIMARY KEY,
    clear_tapes INT,
    branded_tapes INT,
    plastic_bags_small INT,
    carton_boxes_small INT,
    carton_boxes_medium INT,
    carton_boxes_large INT,
    plastic_bags_medium INT,
    kg_90_suck INT,
    kg_50_suck INT
);
 
 INSERT INTO profit ( Num , clear_tapes, branded_tapes, plastic_bags_small, carton_boxes_small,
    carton_boxes_medium, carton_boxes_large, plastic_bags_medium, kg_90_suck, kg_50_suck)
 VALUES (1, 11, 20, 1, 2, 4, 6, 1, 9, 7);
 
  SELECT 
    SUM(clear_tapes) * (SELECT 
            clear_tapes
        FROM
            buying_price) + SUM(branded_tapes) * (SELECT 
            branded_tapes
        FROM
            buying_price) + SUM(plastic_bags_small) * (SELECT 
            plastic_bags_small
        FROM
            buying_price) + SUM(carton_boxes_small) * (SELECT 
            carton_boxes_small
        FROM
            buying_price) + SUM(carton_boxes_medium) * (SELECT 
            carton_boxes_medium
        FROM
            buying_price) + SUM(carton_boxes_large) * (SELECT 
            carton_boxes_large
        FROM
            buying_price) + SUM(plastic_bags_medium) * (SELECT 
            plastic_bags_medium
        FROM
            buying_price) + SUM(kg_90_suck) * (SELECT 
            kg_90_suck
        FROM
            buying_price) + SUM(kg_50_suck) * (SELECT 
            kg_50_suck
        FROM
            buying_price) AS total_cost,
            
            SUM(clear_tapes) * (SELECT 
            clear_tapes
        FROM
            profit) + SUM(branded_tapes) * (SELECT 
            branded_tapes
        FROM
            profit) + SUM(plastic_bags_small) * (SELECT 
            plastic_bags_small
        FROM
            profit) + SUM(carton_boxes_small) * (SELECT 
            carton_boxes_small
        FROM
            profit) + SUM(carton_boxes_medium) * (SELECT 
            carton_boxes_medium
        FROM
            profit) + SUM(carton_boxes_large) * (SELECT 
            carton_boxes_large
        FROM
            profit) + SUM(plastic_bags_medium) * (SELECT 
            plastic_bags_medium
        FROM
            profit) + SUM(kg_90_suck) * (SELECT 
            kg_90_suck
        FROM
            profit) + SUM(kg_50_suck) * (SELECT 
            kg_50_suck
        FROM
            profit) AS total_profit
FROM
    do_outbound;
    
    
CREATE TABLE sale_table (
    DATE DATE PRIMARY KEY,
    daily_sale INT,
    Orders INT
);   
 
 SELECT 
    *
FROM
    sale_table
    WHERE
    MONTH(DATE) = MONTH(CURDATE())
        AND YEAR(DATE) = YEAR(CURDATE());
    

 delete from do_outbound
 where Orders = 222;
 
drop table exp;