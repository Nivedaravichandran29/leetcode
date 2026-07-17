-- Last updated: 7/17/2026, 3:05:50 PM
select distinct author_id as id from Views
where author_id = viewer_id 
order by id;