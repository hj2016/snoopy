create table stock_caregory_data as
select
 code,
 concat_ws(',',collect_set(i.industry_name)) as industry_name,
 concat_ws(',',collect_set(c.concept_name)) as concept_name
 from stock_basics s
  left outer join industry_classified i on(s.code=i.code)
  left outer join concept_classified c on(s.code=c.code)
group by s.code;