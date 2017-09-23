select
  s1.code,
  s1.name,
  s1.industry,
  s1.area,
  s1.pe,
  s1.outstanding,
  s1.totals,
  s1.totalAssets,
  s1.liquidAssets,
  s1.fixedAssets,
  s1.reserved,
  s1.reservedPerShare,
  s1.esp,
  s1.bvps,
  s1.pb,
  s1.timeToMarket,
  s1.undp,
  s1.perundp,
  s1.rev,
  s1.profit,
  s1.gpr,
  s1.npr,
  s1.holders,

  l7.sdate,
  l7.open,
  l7.high,
  l7.close,
  l7.low,
  l7.volume,
  l7.price_change,
  l7.p_change,
  l7.ma5,
  l7.ma10,
  l7.ma20,
  l7.v_ma5,
  l7.v_ma10,
  l7.v_ma20,
  l7.turnover,


  l8.industry_name,
  l8.concept_name,

  l1.eps_yoy,
  l1.epcf,
  l1.profits_yoy,
  l1.distrib,
  l1.report_date,
  l1.report_data_dt,

  l2.roe,
  l2.net_profit_ratio,
  l2.gross_profit_rate,
  l2.net_profits,
  l2.business_income,
  l2.bips,
  l2.profit_data_dt,

  l3.arturnover,
  l3.arturndays,
  l3.inventory_turnover,
  l3.inventory_days,
  l3.currentasset_turnover,
  l3.currentasset_days,
  l3.operation_data_dt,

  l4.mbrg,
  l4.nprg,
  l4.nav,
  l4.targ,
  l4.epsg,
  l4.seg,
  l4.growth_data_dt,

  l5.currentratio,
  l5.quickratio,
  l5.cashratio,
  l5.icratio,
  l5.sheqratio,
  l5.adratio,
  l5.debtpaying_data_dt,

  l6.cf_sales,
  l6.rateofreturn,
  l6.cf_nm,
  l6.cf_liabilities,
  l6.cashflowratio,
  l6.cashflow_data_dt

 from stock_basics s1
  left outer join l_report_data l1 on(s1.code=l1.code)
  left outer join l_profit_data l2 on(s1.code=l2.code)
  left outer join l_operation_data l3 on(s1.code=l3.code)
  left outer join l_growth_data l4 on(s1.code=l4.code)
  left outer join l_debtpaying_data l5 on(s1.code=l5.code)
  left outer join l_cashflow_data l6 on(s1.code=l6.code)
  left outer join last_hist_data l7 on(s1.code=l7.code)
  left outer join stock_caregory_data l8 on(s1.code=l7.code);