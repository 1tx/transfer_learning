import shapefile
import shapely.geometry as geometry
import pandas as pd
# from mpl_toolkits.basemap import Basemap
import matplotlib
import numpy as np
import pylab as plt

# def shapeFile():
#     height = 54
#     width = 66
#     dataxnew = np.load('dataxnew.npy')
#     dataynew = np.load('dataynew.npy')
#     sz_shp = shapefile.Reader(r'../../china-shapefiles/china_country')
#     for city_rcd in sz_shp.shapeRecords():  # 遍历每一条shaperecord
#         if city_rcd.record[5] == 'CHINA':  # 遍历时，record字段是地区的信息（由字符串表示）
#             sz_shp = city_rcd.shape  # 遍历时，shape字段是shape——形状（由点组成）
#
#     grid_lon, grid_lat = np.meshgrid(dataxnew, dataynew)  # 构成了一个坐标矩阵，实际上也就是一个网格，两者是同型矩阵
#     flat_lon = grid_lon.flatten()  # 将坐标展成一维
#     flat_lat = grid_lat.flatten()
#
#     m3 = Basemap(llcrnrlon=77, llcrnrlat=3, urcrnrlon=140, urcrnrlat=51, projection='lcc', lat_1=33, lat_2=45,
#                  lon_0=100)
#     m3.readshapefile("../../china-shapefiles/china_country", 'china', drawbounds=True)
#
#     m3.scatter(flat_lon, flat_lat, latlon=True, s=60, marker="o")  # latlon这个参数指明我传入的数据是经纬度，默认是像素点坐标
#     # np.column_stack((a,b)):向矩阵a增加列，b是增加的部分，将1维数组转换成2维，这样flat的每个点对应上面xi,yi的所有点
#     flat_points = np.column_stack((flat_lon, flat_lat))
#
#     array_index = np.zeros(height * width, dtype=int)
#     i = -1
#     for pt in flat_points:
#         i = i + 1
#         print(i)
#         # make a point and see if it's in the polygon
#         if geometry.Point(pt).within(geometry.shape(sz_shp)):
#             array_index[i] = 1
#             print("The point is in SZ")
#         else:
#             array_index[i] = 0
#             print("The point is not in SZ")
#
#     print(array_index)
#     array_index = array_index.reshape(height, width)
#     np.save('A.npy', array_index)
#     print('end')


def shapefileAll(ALLtestData):
    # shapeFile()
    loadData = np.load('../../jilin.npy')
    loadData = loadData[10:60, 10:100]
    for i in range(len(ALLtestData)):
        ALLtestData[i] = np.multiply(ALLtestData[i], loadData)
    return ALLtestData



        

