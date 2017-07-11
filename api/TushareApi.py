# -*- coding: UTF-8 -*-
__author__ = 'huang jing'
import tushare as ts
from datetime import datetime
class TushareApi:
    path="/home/huangjing/data/"

    @staticmethod
    def get_hist_data(self,start=None, end=None,
                  ktype='D', retry_count=3,
                  pause=0.001):

        stocks = ts.get_stock_basics()
        for stock in stocks.index:
            stockInfo = ts.get_h_data(code=stock,start=start,end=end)
            if(not stockInfo is None):
                dataPath=self.path+"hist_data/"+str(stock)+".csv"
                stockInfo.to_csv(dataPath,header=False)



if __name__ == '__main__':
    """
    a=datetime.now()
    df = ts.get_hist_data('000875')
    df.to_csv('/home/huangjing/data/000875.csv')
    b=datetime.now()
    print (b-a).microseconds
    df=ts.get_h_data(600848)
    print df.shape[0]
    """
    TushareApi.get_hist_data('2017-07-07','2017-07-08')
