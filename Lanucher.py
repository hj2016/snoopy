# vim: set fileencoding=utf-8
__author__ = 'huang jing'

import sys
import api.TushareApi as api
import logging
import time
import util.Logger as log


def callApi(param):
    if len(sys.argv) < 4:
        return False

    apiName = param[1]
    startDate = param[2]
    endDate = param[3]
    if len(sys.argv) > 4:
        api.path = param[4]

    if not hasattr(api.TushareApi, apiName):
        # 方法不存在
        logging.error("%s 方法不存在", apiName)
        return False

    ret = getattr(api.TushareApi, apiName)
    try:
        logging.info("调用 %s 方法", apiName)

        start = time.clock()
        ret(startDate, endDate)

        logging.info('调用 %s 方法用时 %s 秒', apiName ,time.clock() - start)
        return True
    except Exception as err:
        logging.error(err)
        return False


if __name__ == '__main__':
    log.Logger.initLogger()
    reload(sys)
    sys.setdefaultencoding('utf-8')
    logging.info("init......")
    callApi(sys.argv)
