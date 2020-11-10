import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
#from dir3 import file3
import utils
#from package.utils import return_file_path
folder =   '..\\IOT_data\\ori_data'#r'D:\\zyh\\_workspace\\IOT_data\\ori_data'
#print(folder)
class Pipeline:
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        return self.func(other)


#@Pipeline
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
    data = np_data
    return np_data 
#@Pipeline
def describe(data):
    col_names = [
        "ID","2-时间","3-1级区域","4-2级区域","5-3级区域","6-4级区域","7-温度过高","8-温度预警","15-箱门告警","16-防雷告警",
        "18-风扇故障","19-网络设备异常","20-视频1网络异常","21-补光灯异常开启","22-补光灯异常关闭","23-视频2网络异常","24-视频3网络异常",
        "25-视频4网络异常","26-视频5网络异常","27-视频6网络异常","28-温度低","29-监控网络连接异常","30-市电异常","longtitude","magtitude"]
    
    df_with_column_name = pd.DataFrame(data,columns=col_names)   
    print(df_with_column_name.shape)

   # df_with_column_name = df_with_column_name.drop(columns = [])
    
    df_with_column_name = df_with_column_name.drop(columns = ["5-3级区域","6-4级区域","3-1级区域","4-2级区域","2-时间","longtitude","magtitude"])
    print(df_with_column_name.shape)
    #print(df_with_column_name.columns)
    df_gb_id = df_with_column_name.groupby('ID').sum()
    df_gb_id.to_csv('all_gb_id_sum.csv')

    df_count_label = df_gb_id.sum().describe()
    
    df_count_id = df_gb_id.sum(axis=1).describe()

    print('id',df_count_id,df_count_id.shape,'label',df_count_label,df_count_label.shape)
    
    df_gb_id.to_csv('all_gb_id_sum_ALL.csv')
    df_count_label.to_csv('df_count_label_ALL.csv')
    df_count_id.to_csv('df_count_id_ALL.csv')
    #df_gb_id_unstack = df_gb_id.unstack()

    array = np.array(df_gb_id)
    print(
        type(df_gb_id)
        ,df_gb_id.shape
        ,type(array)
        ,array.shape
        
        )

    return data
def find_value_data(file_path):

    
    df = pd.read_csv(file_path)

    df = df.astype('int')
    df=df.set_index(['ID'])

    replace = df.replace(0,np.nan)
    replace = replace[replace>10]
    df = replace.dropna(how= 'all')

  
    value_id = df.describe()

    df.to_csv('none_zero_id_bigger10.csv')
def show_value_data(gps_file,id_file):
    gps = pd.read_csv(gps_file,index_col= 0 ,header = None)
    gps = gps.iloc[:,1:]
    #gps =pd.DataFrame( gps,columns=['ID','L','M'])

    id_data = pd.read_csv(id_file,index_col='ID')

    value_gps =gps[gps.index.isin(id_data.index)]
    print(value_gps)
    value_gps.columns=list('LM')
    value_gps.plot.scatter(x='L',y='M')
    #plt.scatter(x=value_gps.L,y=value_gps.M)
    plt.show()

    
show_value_data('full_gps_data.csv','none_zero_id_bigger10.csv')

#find_value_data('D:\\zyh\\_workspace\\IOT\\all_gb_id_sum_ALL.csv')
#describe(load(folder))
#print(load(folder))
'''
result = folder \
         | load \
         | describe



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
