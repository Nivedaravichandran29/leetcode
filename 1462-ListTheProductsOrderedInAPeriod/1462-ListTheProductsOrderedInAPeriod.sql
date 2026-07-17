-- Last updated: 7/17/2026, 3:05:44 PM
# Write your MySQL query statement below
select p.product_name, sum(o.unit) as unit from Products as p  Join 
 Orders as o
 using(product_id)
WHERE o.order_date >= '2020-02-01' AND o.order_date < '2020-03-01'
 group by product_name
 having sum(o.unit)>=100;
