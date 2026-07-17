-- Last updated: 7/17/2026, 3:06:34 PM
# Write your MySQL query statement below
select name from Employee
where id IN ( select managerId from Employee
group by managerId
having count(*)>=5);