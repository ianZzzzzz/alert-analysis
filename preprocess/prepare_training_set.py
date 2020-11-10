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
    df.columns = list(['time'])
    df = df.sortby('time')
    # sclice
    df_train = df[df.time <= time_point]
    err_label = df[df.time > time_point]

    # sum
    df_id = df_train.groupby('id').sum()
    #这里gb必须是纯err数据 不含区域 要fix之前的错误
    #去掉df里的区域经纬度 另存一个表 后面加上
