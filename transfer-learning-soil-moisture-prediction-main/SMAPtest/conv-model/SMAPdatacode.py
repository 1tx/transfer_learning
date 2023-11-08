import numpy as np
import os

def generatedataSMAP(datadir):
    # 遍历数据集文件夹
    npyfiles = os.listdir(datadir)
    # 初始化数据集
    rawdata=[]
    i=1
    for file in npyfiles:
        path = os.path.join(datadir, file)
        temp_rawdata = np.load(path)
        if i==1:
            rawdata=temp_rawdata
            ###替换数据海洋区域的异常值
            rawdata[rawdata[:] <-0.001] = 0
            i = i + 1
        else:
            rawdata = np.concatenate((rawdata, temp_rawdata), axis=1)
            ###替换数据海洋区域的异常值
            rawdata[rawdata[:] <-0.001] = 0
    return rawdata



