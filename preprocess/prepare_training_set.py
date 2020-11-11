import pandas as pd
import numpy as np
import matplotlib as plt
import utils
'''
pipeline

log_file_path
 # preprocess
    |   load_merge 
    |   slice_timepoint
    |   groupby_id 
    |   sum_base_id
    |   load_to_set

 # train_process
    |   LogisticRegression
 # score_the_result
    |   plot_roc

'''
def load_merge(folder_path):
    file_list = utils.return_file_path(folder_path) # get file path
    print(file_list)
    data_frame = pd.DataFrame([]) #df init 
    print('df init')

    #a+
    for file_name in file_list: 

        data = pd.read_csv(file_name,sep=",",header=None, encoding="gb2312")
        print('successful load',file_name)

        data_frame = data_frame.append(data)
        print('already load dataframe shape',data_frame.shape)

    print('append finish')
    return data_frame 
""" 
    np_data = np.array(data_frame)
    print('numpy convert finish')

    print('numpy array shape',np_data.shape)
    if np_data.shape == data_frame.shape:
        print('Successful convert! np_data.shape == data_frame.shape')
    data = np_data
    return np_data  """

def slice_time_point(df):
    time_point = 1912061200
    df.columns = list( [
        "id","time","area3","area4","area5","6-4级区域","7-温度过高","8-温度预警","15-箱门告警","16-防雷告警",
        "18-风扇故障","19-网络设备异常","20-视频1网络异常","21-补光灯异常开启","22-补光灯异常关闭","23-视频2网络异常","24-视频3网络异常",
        "25-视频4网络异常","26-视频5网络异常","27-视频6网络异常","28-温度低","29-监控网络连接异常","30-市电异常","longtitude","magtitude"]) 
    
    
    
    df.set_index('id')
    df = df.dorp(["area3","area4","area5","6-4级区域","longtitude","magtitude"])
    df.sort_values(by = 'time',ascending = True ,inplace = True)

    # sclice gb.sum
    df_train = df[df.time <= time_point]
    err_label = df[df.time > time_point]
    df_train_gb = df_train.groupby('id').sum()
    err_label_gb = err_label.groupby('id').sum()

    
    
    #去掉df里的区域经纬度 另存一个表 后面加上

    location = pd.read_csv('location_file',index_col='id')
    #useful_location = location[location.id.isin(df_id.id)]
    df_train_gb['father','sun','longtitude','magtitude'] = []

    df_train_gb.set_index('id')
    
    for i in enumerate(df_train_gb.index):
        df_train_gb[i]['father','sun','longtitude','magtitude'] = 
            location[i]['father','sun','longtitude','magtitude']
    
    err_label_gb.set_index('id')
    err_label['sum'] = err_label_gb.sum(axis =1)
    err_label['label'][err_label.sum<10] = 0
    err_label['label'][err_label.sum>=0] = 1

    err_label.to_csv('set.csv')
    