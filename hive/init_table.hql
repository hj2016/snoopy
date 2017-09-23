create table stock_basics(
  code string comment '代码',
  name string comment '名称',
  industry string comment '所属行业',
  area string comment '地区',
  pe double comment '市盈率',
  outstanding double comment '流通股本(亿)',
  totals double comment '总股本(亿)',
  totalAssets double comment '总资产(万)',
  liquidAssets double comment '流动资产',
  fixedAssets double comment '固定资产',
  reserved double comment '公积金',
  reservedPerShare double comment '每股公积金',
  esp double comment '每股收益',
  bvps double comment '每股净资',
  pb double comment '市净率',
  timeToMarket string comment '上市日期',
  undp double comment '未分利润',
  perundp string comment ' 每股未分配',
  rev double comment '收入同比(%)',
  profit double comment '利润同比(%)',
  gpr double comment '毛利率(%)',
  npr double comment '净利润率(%)',
  holders double comment '股东人数'
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';


create table hist_data(
  sdate string comment '日期YYYY-MM-dd',
  code string comment '股票代码',
  open double comment '开盘价',
  high double comment '最高价',
  close double comment '收盘价',
  low double comment '最低价',
  volume double comment '成交量',
  price_change double comment '价格变动',
  p_change double comment '涨跌幅',
  ma5 double comment '5日均价',
  ma10 double comment '10日均价',
  ma20 double comment '20日均价',
  v_ma5 double comment '5日均量',
  v_ma10 double comment '10日均量',
  v_ma20 double comment '20日均量',
  turnover double comment '换手率')
PARTITIONED BY (`dt` string comment '日期YYYY-MM' )
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';


create table industry_classified(
  sindex string comment '序号',
  code string comment '股票代码',
  name string comment '股票名称',
  industry_name string comment '行业名称'
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';


create table concept_classified(
  sindex string comment '序号',
  code string comment '股票代码',
  name string comment '股票名称',
  concept_name string comment '概念名称'
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';


create table report_data (
  sindex string comment '编号',
  code string comment '代码',
  name string comment '名称',
  esp double comment '每股收益',
  eps_yoy double comment '每股收益同比(%)',
  bvps double comment '每股净资产',
  roe double comment '净资产收益率(%)',
  epcf double comment '每股现金流量(元)',
  net_profits double comment '净利润(万元)',
  profits_yoy double comment '净利润同比(%)',
  distrib string comment '分配方案',
  report_date string comment '发布日期',
  report_data_dt string comment '季报日期'
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';


create table profit_data (
  sindex string comment '编号',
  code string comment '代码',
  name string comment '名称',
  roe double comment '净资产收益率(%)',
  net_profit_ratio double comment '净利率(%)',
  gross_profit_rate double comment '毛利率(%)',
  net_profits double comment '净利润(万元)',
  esp double comment '每股收益',
  business_income double comment '营业收入(百万元)',
  bips double comment '每股主营业务收入(元)',
  profit_data_dt string comment '季报日期'
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';



create table operation_data(
  sindex string comment '编号',
  code string comment '代码',
  name string comment '名称',
  arturnover double comment '应收账款周转率(次)',
  arturndays double comment '应收账款周转天数(天)',
  inventory_turnover double comment '存货周转率(次)',
  inventory_days double comment '存货周转天数(天)',
  currentasset_turnover double comment '流动资产周转率(次)',
  currentasset_days double comment '流动资产周转天数(天)',
  operation_data_dt string comment '季报日期'
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';



create table growth_data(
  sindex string comment '编号',
  code string comment '代码',
  name string comment '名称',
  mbrg double comment '主营业务收入增长率(%)',
  nprg double comment '净利润增长率(%)',
  nav double comment '净资产增长率',
  targ double comment '总资产增长率',
  epsg double comment '每股收益增长率',
  seg double comment '股东权益增长率',
  growth_data_dt string comment '季报时间'
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';


create table debtpaying_data(
  sindex string comment '编号',
  code string comment '代码',
  name string comment '名称',
  currentratio double comment '流动比率',
  quickratio double comment '速动比率',
  cashratio double comment '现金比率',
  icratio double comment '利息支付倍数',
  sheqratio double comment '股东权益比率',
  adratio double comment '股东权益增长率',
  debtpaying_data_dt string comment '季报时间'
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';


create table cashflow_data(
  sindex string comment '编号',
  code string comment '代码',
  name string comment '名称',
  cf_sales double comment '经营现金净流量对销售收入比率',
  rateofreturn double comment '资产的经营现金流量回报率',
  cf_nm double comment '经营现金净流量与净利润的比率',
  cf_liabilities double comment '经营现金净流量对负债比率',
  cashflowratio double comment '现金流量比率',
  cashflow_data_dt string comment '季报时间'
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';


create table stock_tag(
  --stock基本数据
  --stock_basics
  code string comment '代码',
  name string comment '名称',
  industry string comment '所属行业',
  area string comment '地区',
  pe double comment '市盈率',
  outstanding double comment '流通股本(亿)',
  totals double comment '总股本(亿)',
  totalAssets double comment '总资产(万)',
  liquidAssets double comment '流动资产',
  fixedAssets double comment '固定资产',
  reserved double comment '公积金',
  reservedPerShare double comment '每股公积金',
  esp double comment '每股收益',
  bvps double comment '每股净资',
  pb double comment '市净率',
  timeToMarket string comment '上市日期',
  undp double comment '未分利润',
  perundp string comment ' 每股未分配',
  rev double comment '收入同比(%)',
  profit double comment '利润同比(%)',
  gpr double comment '毛利率(%)',
  npr double comment '净利润率(%)',
  holders double comment '股东人数',

  --行情数据
  --hist_data
  sdate string comment '日期YYYY-MM-dd',
  open double comment '开盘价',
  high double comment '最高价',
  close double comment '收盘价',
  low double comment '最低价',
  volume double comment '成交量',
  price_change double comment '价格变动',
  p_change double comment '涨跌幅',
  ma5 double comment '5日均价',
  ma10 double comment '10日均价',
  ma20 double comment '20日均价',
  v_ma5 double comment '5日均量',
  v_ma10 double comment '10日均量',
  v_ma20 double comment '20日均量',
  turnover double comment '换手率',

  --股票分类
  --industry_classified
  industry_name string comment '行业名称',

  --concept_classified
  concept_name string comment '概念名称',

  --基本面数据
  --report_data(业绩报告)
  --esp double comment '每股收益',
  eps_yoy double comment '每股收益同比(%)',
  --bvps double comment '每股净资产',
  --roe double comment '净资产收益率(%)',
  epcf double comment '每股现金流量(元)',
  --net_profits double comment '净利润(万元)',
  profits_yoy double comment '净利润同比(%)',
  distrib string comment '分配方案',
  report_date string comment '发布日期',
  report_data_dt string comment '季报日期',

  --profit_data(盈利能力)
  roe double comment '净资产收益率(%)',
  net_profit_ratio double comment '净利率(%)',
  gross_profit_rate double comment '毛利率(%)',
  net_profits double comment '净利润(万元)',
  --esp double comment '每股收益',
  business_income double comment '营业收入(百万元)',
  bips double comment '每股主营业务收入(元)',
  profit_data_dt string comment '季报日期',

  --operation_data(营运能力)
  arturnover double comment '应收账款周转率(次)',
  arturndays double comment '应收账款周转天数(天)',
  inventory_turnover double comment '存货周转率(次)',
  inventory_days double comment '存货周转天数(天)',
  currentasset_turnover double comment '流动资产周转率(次)',
  currentasset_days double comment '流动资产周转天数(天)',
  operation_data_dt string comment '季报日期',

  --growth_data(成长能力)
  mbrg double comment '主营业务收入增长率(%)',
  nprg double comment '净利润增长率(%)',
  nav double comment '净资产增长率',
  targ double comment '总资产增长率',
  epsg double comment '每股收益增长率',
  seg double comment '股东权益增长率',
  growth_data_dt string comment '季报时间',


  --debtpaying_data(偿债能力)
  currentratio double comment '流动比率',
  quickratio double comment '速动比率',
  cashratio double comment '现金比率',
  icratio double comment '利息支付倍数',
  sheqratio double comment '股东权益比率',
  adratio double comment '股东权益增长率',
  debtpaying_data_dt string comment '季报时间',

  --cashflow_data(现金流量)
  cf_sales double comment '经营现金净流量对销售收入比率',
  rateofreturn double comment '资产的经营现金流量回报率',
  cf_nm double comment '经营现金净流量与净利润的比率',
  cf_liabilities double comment '经营现金净流量对负债比率',
  cashflowratio double comment '现金流量比率',
  cashflow_data_dt string comment '季报时间'
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';