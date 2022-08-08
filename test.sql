--sql

delete from user
where id = 2; 


--try SQLi 
insert into user values(2, "emal@asas.com", "admin1", "admin", "password' or 1=1"); 

select * from user;