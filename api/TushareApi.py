# -*- coding: UTF-8 -*-
__author__ = 'huang jing'
import tushare as ts
import sys
from datetime import datetime


class TushareApi:
    path = "/home/huangjing/data/"

    @staticmethod
    def get_hist_data(self, start=None, end=None):

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
    """

    reload(sys)
    sys.setdefaultencoding('utf-8')
    TushareApi.get_stock_basics()
    ts.get_report_data()
