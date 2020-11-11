import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
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
    |
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
    time_point = 1912051200
    data_name = list([ "id","time","area3","area4","area5","6-4级区域",'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',"longtitude","magtitude" ] 
    )
    df.columns = data_name
    print('col name set')
    df = df.drop(columns = ["area3","area4","area5","6-4级区域","longtitude","magtitude"])
    print('useless col drop')
    df.sort_values(by = 'time',ascending = True ,inplace = True)
    print('sort by time')
    print('sclice gb.sum')

    df_train = df[df.time <= time_point]
    err_label = df[df.time > time_point]
    print('silice finish')
    df_train_gb = df_train.groupby('id').sum()
    err_label_gb = err_label.groupby('id').sum() #dfg
    print('gb sum finish')
    label = err_label_gb.sum(axis = 1) # 求各id 的总告警数量
    print('axis =1 finish')
    label = label[label>10] # np array
    print('>10')
    Y= pd.DataFrame (df_train_gb.index)
    print('init Y.index')
    Y['label'] = label.index.isin(Y.index)

    print('init Y.label')



    
    train_data = df_train_gb.values # np array
    
    X = train_data
    Y = Y.values
    print('xy ready')
    
    train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size=0.2)
    print(train_x,test_x,train_y,test_y)


    
    """ 
    
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
     """


slice_time_point( load_merge('D:\\zyh\\_workspace\\IOT_data\\logs3days'))