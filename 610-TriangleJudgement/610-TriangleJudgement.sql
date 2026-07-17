-- Last updated: 7/17/2026, 3:06:20 PM
select *, if(x+y>z and y+z>x and x+z>y, "Yes","No") as triangle from triangle