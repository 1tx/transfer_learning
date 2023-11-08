import numpy as np
from shapefileUtil import shapefileAll

def compute_rmse_r2(data_testd_y,pred):
    data_testd_y[data_testd_y<=0]=0
    loadData = np.load('../../jilin.npy')
    loadData = loadData[10:60, 10:100]
    # loadData = loadData[150:209, 200:409]
    # loadData = loadData[200: 259, 450:659]
    num = np.sum(loadData == 1)
    pred = shapefileAll(pred)
    data_testd_y = shapefileAll(data_testd_y)
    # 计算RMSE
    rmsemap = np.sqrt(np.mean(((data_testd_y - pred) ** 2), 0))
    rmse = np.sum(rmsemap) / num
    # 计算MAE
    maeemap = np.mean(np.abs(data_testd_y - pred), 0)
    mae = np.sum(maeemap) / num
    # R2
    b = (data_testd_y - pred) ** 2
    sum = 0
    ww=np.var(data_testd_y[2])
    for i in range(len(data_testd_y)):
        sum = sum + np.var(data_testd_y[i])

    a = sum / len(data_testd_y)
    # a = np.var(data_testd_y)
    r2map = np.mean(1 - (b / a), axis=0)
    r2map = np.multiply(r2map, loadData)
    r2 = np.sum(r2map) / num
    print(f"均方误差(RMSE)：{rmse}")
    print(f"均方误差(MAE)：{mae}")
    print(f"测试集R^2：{r2}")



