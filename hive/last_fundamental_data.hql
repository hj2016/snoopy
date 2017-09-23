drop table if exists l_report_data;
create table l_report_data as
select t1.* from report_data t1 join (select code,max(dt) as dt from report_data group by code) t2 on(t1.code=t2.code and t1.dt=t2.dt);

drop table if exists l_profit_data;
create table l_profit_data as
select t1.* from profit_data t1 join (select code,max(dt) as dt from profit_data group by code) t2 on(t1.code=t2.code and t1.dt=t2.dt);

drop table if exists l_operation_data;
create table l_operation_data as
select t1.* from operation_data t1 join (select code,max(dt) as dt from operation_data group by code) t2 on(t1.code=t2.code and t1.dt=t2.dt);

drop table if exists l_growth_data;
create table l_growth_data as
select t1.* from growth_data t1 join (select code,max(dt) as dt from growth_data group by code) t2 on(t1.code=t2.code and t1.dt=t2.dt);

drop table if exists l_debtpaying_data;
create table l_debtpaying_data as
select t1.* from debtpaying_data t1 join (select code,max(dt) as dt from debtpaying_data group by code) t2 on(t1.code=t2.code and t1.dt=t2.dt);

drop table if exists l_cashflow_data;
create table l_cashflow_data as
select t1.* from cashflow_data t1 join (select code,max(dt) as dt from cashflow_data group by code) t2 on(t1.code=t2.code and t1.dt=t2.dt);


