# -*- coding: UTF-8 -*-
__author__ = 'huang jing'
import tushare as ts
import sys
import util.DataUtil as dataUtil
from datetime import datetime


class TushareApi:
    path = "/home/huangjing/data/"

    @staticmethod
    def get_hist_data(start=None, end=None):

        stocks = ts.get_stock_basics()
        for stock in stocks.index:
            stockInfo = ts.get_h_data(code=stock, start=start, end=end)
            if (not stockInfo is None):
                dataPath = TushareApi.path + "hist_data/" + str(stock) + ".csv"
                stockInfo.to_csv(dataPath, header=False)

    @staticmethod
    def get_industry_classified():
        df = ts.get_industry_classified()
        dataPath = TushareApi.path + "industry_classified/" + "industry_classified.csv"
        df.to_csv(dataPath, header=False)

    @staticmethod
    def get_concept_classified():
        df = ts.get_concept_classified()
        dataPath = TushareApi.path + "concept_classified/" + "concept_classified.csv"
        df.to_csv(dataPath, header=False)

    @staticmethod
    def get_stock_basics():
        df = ts.get_stock_basics()
        dataPath = TushareApi.path + "stock_basics/" + "stock_basics.csv"
        df.to_csv(dataPath, header=False)

    @staticmethod
    def get_report_data(start=None, end=None):
        startArr = start.split("-")
        endArr = end.split("-")
        seasonList = dataUtil.getListSeason(int(startArr[0]), int(startArr[1]), int(endArr[0]), int(endArr[1]))
        for season in seasonList :
            df = ts.get_report_data(season[0],season[1])
            dataPath = TushareApi.path + "report_data/" + "report_data_"+season[0]+"_"+season[1]+".csv"
            df.to_csv(dataPath, header=False)


    @staticmethod
    def get_profit_data(start=None, end=None):

        startArr = start.split("-")
        endArr = end.split("-")
        seasonList = dataUtil.getListSeason(int(startArr[0]), int(startArr[1]), int(endArr[0]), int(endArr[1]))
        for season in seasonList :
            df = ts.get_profit_data(season[0],season[1])
            dataPath = TushareApi.path + "profit_data/" + "profit_data_"+season[0]+"_"+season[1]+".csv"
            df.to_csv(dataPath, header=False)

    @staticmethod
    def get_operation_data(start=None, end=None):
        dataPath = TushareApi.path + "operation_data/" + "operation_data.csv"
        startArr = start.split("-")
        endArr = end.split("-")
        seasonList = dataUtil.getListSeason(int(startArr[0]), int(startArr[1]), int(endArr[0]), int(endArr[1]))
        for season in seasonList :
            df = ts.get_operation_data(season[0],season[1])
            df.to_csv(dataPath, header=False)

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
    TushareApi.get_report_data('2016-01-01','2017-01-01')
