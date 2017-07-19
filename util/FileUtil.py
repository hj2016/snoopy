# -*- encoding:utf8 -*-
'''
@author: huangjing
@version: 2013-10-12
'''
import os
'''
    如果不存在创建目录
'''
def isNotExisMkPath(filepath):
    path = filepath[0:filepath.rindex("/")]
    if not os.path.exists(path):
        os.makedirs(path)
'''
    保存dataFrame文件
'''
def saveDf(df,filepath):
    isNotExisMkPath(filepath)
    df.to_csv(filepath, header=False)


if __name__ == '__main__':
    isNotExisMkPath("/home/huangjing/data/a/b/bcc.txt")
