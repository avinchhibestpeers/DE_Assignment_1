--  question one
select site_name,
       sum(case when therapeutic_area = "oncology" then 1 else 0 end) / count(*) as oncology_rate
from Logs
where site_category = "academic"
group by site_name;


-- question two
select x.site_name, count(*)
from (select
          site_name,
          date(created_at) event_date,
          min(date(created_at)) over (partition by site_name) as min_date
    from Logs) as x
where event_date between min_date and adddate(min_date, 14)
group by site_name
having count(*) >= 10;

