create table last_hist_data as
select * from hist_data where sdate="${sdate}" and dt="${dt}";