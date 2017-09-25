# -*- coding: UTF-8 -*-
__author__ = 'huang jing'
import tushare as ts
import sys
import util.DataUtil as dataUtil
from datetime import datetime
import numpy as np
import pandas as pd
import util.Logger as log
import util.FileUtil as fileUtil

class TushareApi:
    path = "/home/huangjing/data/"

    @staticmethod
    def get_hist_data(start=None, end=None):

        stocks = ts.get_stock_basics()

        tmonths= dataUtil.getListMonth(start,end)

        for tmonth in tmonths :

            for stock in stocks.index :
                stockInfo = ts.get_hist_data(code=stock, start=tmonth[1], end=tmonth[2])

                if (not stockInfo is None and not len(stockInfo) == 0):
                    code = pd.DataFrame({"code": np.array([stock]*len(stockInfo))},index=stockInfo.index)
                    df = pd.concat([code,stockInfo],axis=1)
                    #dataPath = TushareApi.path + "hist_data/dt=" + str(tmonth[0]) + "/" + str(stock) + ".csv"
                    dataPath = TushareApi.path + "hist_data/dt=" + str(tmonth[0]) + "/stock.csv"
                    fileUtil.saveDf(df,dataPath,"a")

    @staticmethod
    def get_industry_classified(start=None, end=None ):
        df = ts.get_industry_classified()
        dataPath = TushareApi.path + "industry_classified/" + "industry_classified.csv"
        fileUtil.saveDf(df,dataPath)

    @staticmethod
    def get_concept_classified(start=None, end=None):
        df = ts.get_concept_classified()
        dataPath = TushareApi.path + "concept_classified/" + "concept_classified.csv"
        fileUtil.saveDf(df,dataPath)

    @staticmethod
    def get_stock_basics(start=None, end=None):
        df = ts.get_stock_basics()
        dataPath = TushareApi.path + "stock_basics/" + "stock_basics.csv"
        fileUtil.saveDf(df,dataPath)

    @staticmethod
    def get_report_data(start=None, end=None):
        startArr = start.split("-")
        endArr = end.split("-")
        seasonList = dataUtil.getListSeason(int(startArr[0]), int(startArr[1]), int(endArr[0]), int(endArr[1]))
        for season in seasonList :
            df = ts.get_report_data(season[0],season[1]).drop_duplicates('code')
            dt = pd.DataFrame({"date": np.array([str(season[0])+"-"+str(season[1])]*len(df))},index=df.index)

            df = pd.concat([df,dt],axis=1)
            dataPath = TushareApi.path + "report_data/" +str(season[0])+"-"+str(season[1])+"-report_data.csv"
            fileUtil.saveDf(df,dataPath)

    @staticmethod
    def get_profit_data(start=None, end=None):

        startArr = start.split("-")
        endArr = end.split("-")
        seasonList = dataUtil.getListSeason(int(startArr[0]), int(startArr[1]), int(endArr[0]), int(endArr[1]))
        for season in seasonList :
            df = ts.get_profit_data(season[0],season[1]).drop_duplicates('code')
            dt = pd.DataFrame({"date": np.array([str(season[0])+"-"+str(season[1])]*len(df))},index=df.index)

            df = pd.concat([df,dt],axis=1)
            dataPath = TushareApi.path + "profit_data/" +str(season[0])+"-"+str(season[1])+"-profit_data.csv"
            fileUtil.saveDf(df,dataPath)

    @staticmethod
    def get_growth_data(start=None, end=None):
        startArr = start.split("-")
        endArr = end.split("-")
        seasonList = dataUtil.getListSeason(int(startArr[0]), int(startArr[1]), int(endArr[0]), int(endArr[1]))
        for season in seasonList :
            df = ts.get_growth_data(season[0],season[1]).drop_duplicates('code')
            dt = pd.DataFrame({"date": np.array([str(season[0])+"-"+str(season[1])]*len(df))},index=df.index)

            df = pd.concat([df,dt],axis=1)
            dataPath = TushareApi.path + "growth_data/" +str(season[0])+"-"+str(season[1])+"-growth_data.csv"
            fileUtil.saveDf(df,dataPath)

    @staticmethod
    def get_debtpaying_data(start=None, end=None):
        startArr = start.split("-")
        endArr = end.split("-")
        seasonList = dataUtil.getListSeason(int(startArr[0]), int(startArr[1]), int(endArr[0]), int(endArr[1]))
        for season in seasonList :
            df = ts.get_debtpaying_data(season[0],season[1]).drop_duplicates('code')
            dt = pd.DataFrame({"date": np.array([str(season[0])+"-"+str(season[1])]*len(df))},index=df.index)

            df = pd.concat([df,dt],axis=1)
            dataPath = TushareApi.path + "debtpaying_data/" +str(season[0])+"-"+str(season[1])+"-debtpaying_data.csv"
            fileUtil.saveDf(df,dataPath)

    @staticmethod
    def  get_cashflow_data(start=None, end=None):
        startArr = start.split("-")
        endArr = end.split("-")
        seasonList = dataUtil.getListSeason(int(startArr[0]), int(startArr[1]), int(endArr[0]), int(endArr[1]))
        for season in seasonList :
            df = ts.get_cashflow_data(season[0],season[1]).drop_duplicates('code')
            dt = pd.DataFrame({"date": np.array([str(season[0])+"-"+str(season[1])]*len(df))},index=df.index)

            df = pd.concat([df,dt],axis=1)
            dataPath = TushareApi.path + "cashflow_data/" +str(season[0])+"-"+str(season[1])+"-cashflow_data.csv"
            fileUtil.saveDf(df,dataPath)

    @staticmethod
    def is_trade_day(day=None):
        df=ts.trade_cal()
        rs = df[df.calendarDate==day]
        return rs.at[rs.index[0],"isOpen"]

    @staticmethod
    def get_operation_data(start=None, end=None):
        startArr = start.split("-")
        endArr = end.split("-")
        seasonList = dataUtil.getListSeason(int(startArr[0]), int(startArr[1]), int(endArr[0]), int(endArr[1]))
        for season in seasonList :
            df = ts.get_operation_data(season[0],season[1]).drop_duplicates('code')
            dt = pd.DataFrame({"date": np.array([str(season[0])+"-"+str(season[1])]*len(df))},index=df.index)

            df = pd.concat([df,dt],axis=1)
            dataPath = TushareApi.path + "operation_data/" +str(season[0])+"-"+str(season[1])+"-operation_data.csv"
            fileUtil.saveDf(df,dataPath)


if __name__ == '__main__':
    """
    a=datetime.now()
    df = ts.get_hist_data('000875')
    df.to_csv('/home/huangjing/data/000875.csv')
    b=datetime.now()
    print (b-a).microseconds
    df=ts.get_h_data(600848)
    print df.shape[0]
    TushareApi.get_hist_data('2017-07-07','2017-07-08')
    TushareApi.get_industry_classified()
    TushareApi.get_concept_classified()
    TushareApi.get_stock_basics()
    """
    reload(sys)

    sys.setdefaultencoding('utf-8')
    # TushareApi.get_hist_data('2017-07-01','2017-07-06')

    TushareApi.get_hist_data('2017-06-01','2017-06-01')

    #TushareApi.get_report_data('2016-01-01','2017-01-01')
    #TushareApi.get_profit_data('2016-01-01','2017-01-01')
    #TushareApi.get_operation_data('2016-01-01','2017-01-01')
    #TushareApi.get_growth_data('2016-01-01','2017-01-01')
    #TushareApi.get_debtpaying_data('2017-01-01','2017-01-02')
    #TushareApi.get_cashflow_data('2016-01-01','2017-01-01')
    #TushareApi.is_trade_day("2017-07-14")

    #ret = getattr(TushareApi,'is_trade_day')
    #print ret("2017-07-14")

    #TushareApi.get_cashflow_data('2017-06-15','2017-06-16')