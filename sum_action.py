import pandas as pd
import numpy as np
import sys
sys.path.append("..")
#from dir3 import file3
from package import utils
#from package.utils import return_file_path
folder =   '..\\IOT_data\\ori_data'#r'D:\\zyh\\_workspace\\IOT_data\\ori_data'
print(folder)
class Pipeline:
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        return self.func(other)


@Pipeline
def load(folder_path):
    
    file_list = utils.return_file_path(folder_path) # get file path
    print(file_list)

    data_frame = pd.DataFrame([]) #df init 
    print('df init')

    for file_name in file_list: 

        data = pd.read_csv(file_name,sep=",",header=None, encoding="gb2312")
        print('successful load',file_name)

        data_frame = data_frame.append(data)
        print('already load dataframe shape',data_frame.shape)

    print('append finish')

    # return data_frame 

    np_data = np.array(data_frame)
    print('numpy convert finish')

    print('numpy array shape',np_data.shape)
    if np_data.shape == data_frame.shape:
        print('Successful convert! np_data.shape == data_frame.shape')

    return np_data 
@Pipeline
def converter(data):
    col_names = [
        "ID","2-时间","3-1级区域","4-2级区域","5-3级区域","6-4级区域","7-温度过高","8-温度预警","15-箱门告警","16-防雷告警",
        "18-风扇故障","19-网络设备异常","20-视频1网络异常","21-补光灯异常开启","22-补光灯异常关闭","23-视频2网络异常","24-视频3网络异常",
        "25-视频4网络异常","26-视频5网络异常","27-视频6网络异常","28-温度低","29-监控网络连接异常","30-市电异常","longtitude","magtitude"]

    df_with_column_name = pd.DataFrame(data,columns=col_names )
    df_gb_id = data.groupby('ID').sum()
    print(df_gb_id)
    return data
#load(folder)
#print(load(folder))

result = folder \
         | load \
         | converter

'''
 #        | \
 #        | write

print(result)

data_names = [
        "1-ID","2-时间","3-1级区域","4-2级区域","5-3级区域","6-4级区域","7-温度过高","8-温度预警","15-箱门告警","16-防雷告警",
        "18-风扇故障","19-网络设备异常","20-视频1网络异常","21-补光灯异常开启","22-补光灯异常关闭","23-视频2网络异常","24-视频3网络异常",
        "25-视频4网络异常","26-视频5网络异常","27-视频6网络异常","28-温度低","29-监控网络连接异常","30-市电异常","longtitude","magtitude"]
data_frame = pd.DataFrame([])
data_frame.append(pd.read_csv('D:\zyh\_workspace\IOT_data\ori_data\\18.log',sep=",",header=None, encoding="gb2312"))
print(data_frame.columns)
ret =list(data_frame.columns)
ret = data_names

data_frame.columns = ret
print(data_frame.columns)'''