drop table if exists l_report_data;
create table l_report_data as
select t1.* from report_data t1 join (select code,max(report_data_dt) as report_data_dt from report_data group by code) t2 on(t1.code=t2.code and t1.report_data_dt=t2.report_data_dt);

drop table if exists l_profit_data;
create table l_profit_data as
select t1.* from profit_data t1 join (select code,max(profit_data_dt) as profit_data_dt from profit_data group by code) t2 on(t1.code=t2.code and t1.profit_data_dt=t2.profit_data_dt);

drop table if exists l_operation_data;
create table l_operation_data as
select t1.* from operation_data t1 join (select code,max(operation_data_dt) as operation_data_dt from operation_data group by code) t2 on(t1.code=t2.code and t1.operation_data_dt=t2.operation_data_dt);

drop table if exists l_growth_data;
create table l_growth_data as
select t1.* from growth_data t1 join (select code,max(growth_data_dt) as growth_data_dt from growth_data group by code) t2 on(t1.code=t2.code and t1.growth_data_dt=t2.growth_data_dt);

drop table if exists l_debtpaying_data;
create table l_debtpaying_data as
select t1.* from debtpaying_data t1 join (select code,max(debtpaying_data_dt) as debtpaying_data_dt from debtpaying_data group by code) t2 on(t1.code=t2.code and t1.debtpaying_data_dt=t2.debtpaying_data_dt);

drop table if exists l_cashflow_data;
create table l_cashflow_data as
select t1.* from cashflow_data t1 join (select code,max(cashflow_data_dt) as cashflow_data_dt from cashflow_data group by code) t2 on(t1.code=t2.code and t1.cashflow_data_dt=t2.cashflow_data_dt);


