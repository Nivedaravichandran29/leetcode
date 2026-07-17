-- Last updated: 7/17/2026, 3:06:22 PM
# Write your MySQL query statement below
/* Write your T-SQL query statement below */
select id,
    case
        when p_id is null then 'Root'
        when id in (select distinct p_id from tree where p_id is not null) then 'Inner'
        else 'Leaf'
    end as type
from Tree