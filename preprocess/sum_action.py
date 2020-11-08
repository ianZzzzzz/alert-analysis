import pandas as pd
from ../ import utils
folder = '..//IOT_dat//ori_data'

def load(folder_path):
    file_list = utils.find_all_file(folder_path)
    data_frame = new pd.DataFrame([])
    for file_name in file_list:
        data_frame.append(
            pd.read_csv(file_name,sep=",",header=None, encoding="gb2312")
        )
    return data_frame
    '''
    '''
    file_list = utils.find_all_file(folder_path)
    dataframe = None
        
    data_names = [
        "1-ID","2-时间","3-1级区域","4-2级区域","5-3级区域","6-4级区域","7-温度过高","8-温度预警","15-箱门告警","16-防雷告警",
        "18-风扇故障","19-网络设备异常","20-视频1网络异常","21-补光灯异常开启","22-补光灯异常关闭","23-视频2网络异常","24-视频3网络异常",
        "25-视频4网络异常","26-视频5网络异常","27-视频6网络异常","28-温度低","29-监控网络连接异常","30-市电异常","longtitude","magtitude"]
    df_1 = pd.read_csv(file_path)
    for file_name in  file_list:
        df = pd.read_csv(file_name,sep=",",header=None, names=data_names, encoding="gb2312"
        df_3= pd.concat[df_1,df]
        df_1= df_3
        # df.to_csv('full_gps_data.csv',index=False, header=False, mode='a+')

    return dataframe;
'''
result = folder \
         | load \
         | converter\
         | write

'''