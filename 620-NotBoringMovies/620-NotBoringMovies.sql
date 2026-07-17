-- Last updated: 7/17/2026, 3:06:18 PM
# Write your MySQL query statement below
select* from Cinema
where id%2!=0 and description!="boring"
order by rating desc ;