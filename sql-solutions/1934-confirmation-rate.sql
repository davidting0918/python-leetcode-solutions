-- https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50

with temp as (
    select
        user_id,
        round(sum(case when action = 'confirmed' then 1 else 0 end) / count(*), 2) as rate
    from Confirmations 
    group by user_id
)
select
    user_id,
    ifnull(rate, 0.0) as confirmation_rate
from Signups
left join temp using (user_id);  