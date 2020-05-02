with unbanned as (
select
    t.Status as status,
    t.Request_at as Day
from Trips t
join Users u on u.users_id = t.Client_Id or u.users_id = t.driver_Id
group by t.Id
having sum(u.banned = 'Yes') = 0
)

select
Day,
ROUND(sum(case when status != 'completed' then 1 else 0 end) / count(*), 2) as "Cancellation Rate"
from unbanned
where
Day between '2013-10-01' and '2013-10-03'
group by Day
