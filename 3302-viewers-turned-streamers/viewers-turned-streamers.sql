with cte as (
select user_id, min(session_start) as min_time from Sessions
group by user_id
),
cte1 as (
select user_id from Sessions
where session_type = "Viewer" and (session_start in (select min_time from cte))),
cte2 as (
select user_id, count(session_type) as sessions_count from Sessions
where session_type = "Streamer" and (user_id in (select * from cte1))
group by user_id
)
select * from cte2
order by sessions_count desc, user_id desc