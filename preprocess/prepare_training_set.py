import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.svm import SVC

from sklearn.model_selection import train_test_split #训练测试集拆分
from sklearn.linear_model import LogisticRegression  #逻辑回归模型 
#from sklearn.externals import joblib #保存加载模型函数joblib
import joblib 
#以下为sklearn评测指标的一些函数
from sklearn.metrics import precision_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import utils
import warnings
warnings.filterwarnings("ignore")

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
    |   plot_result

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
    time_point = 191203100900
    data_name = list([ "id","time","area3","area4","area5","6-4级区域",'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','v','c','','','tem',"longtitude","magtitude" ] 
    )
    df.columns = data_name
  
    df = df.drop(columns = ['v','c','tem',"area3","area4","area5","6-4级区域","longtitude","magtitude"])
    
    df.sort_values(by = 'time',ascending = False ,inplace = True)
 

    df_train = df[df['time'] <= time_point].drop(columns = ['time'])
    err_label = df[df['time'] > time_point].drop(columns = ['time'])

    print('silice finish',
        'df_train shape',df_train.shape,
        'err_label shape',err_label.shape)

    df_train_gb = df_train.groupby('id').sum()
    err_label_gb = err_label.groupby('id').sum() #dfg

    
    label = err_label_gb.sum(axis = 1) # 求各id 的总告警数量
    
    label = label[label>10] # np array
   


    Y= pd.DataFrame ([])
     
    a=0
    b=0
    Y['value'] = []
    Y['index'] = df_train_gb.index
    Y.set_index(['index'],inplace = True)
    
    for i in Y.index:
        if i in label.index :
            Y.loc[i]['value'] = 1
            a=a+1
        else :
            Y.loc[i]['value'] = 0
            b=b+1
    #print(a,b)
    #print(df_train_gb,Y['value'])   
    X = df_train_gb.values
    Y = Y['value'].values

    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.5)
 # 生成模型，并喂入数据
    clf = LogisticRegression()
    clf.fit(x_train, y_train)
 # 保存模型（用joblib，不用pickle）
    joblib.dump(clf,"lr.model")    #from sklearn.externals import joblib
 #加载模型是： clf = joblib.load("lr.model")
 
 
 #6. 预测结果，并评测
    y_pred = clf.predict(x_test)  #预测出来的值计做y_pred
    y_true = y_test               #真实值计做y_true，和sklearn参数一模一样 
    target_names = ['class 0', 'class 1']
    print(classification_report(y_true, y_pred, target_names=target_names)) #可以参考sklearn官网API
    print(confusion_matrix(y_true, y_pred)) #混淆矩阵（记住！sklearn定义的混淆矩阵m行n列含义是：该样本真实值是m，预测值是n）
    
    plt.rcParams['font.sans-serif'] = ['SimHei']   
    plt.rcParams['font.family']='sans-serif' 
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(y_pred,"b.", label = "y_pred")   #blue，点号
    plt.plot(y_true,"r*", label = "y_true")   #red，星号
    plt.legend()
    plt.show() 

    # return X,Y

    #print("X shape",X,type(X),'Y shape',Y,type(Y))
    #print('xy ready')
    """ 
        train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size=0.2)
        print('train_x',train_x,'test_x',test_x,'train_y',train_y,'test_y',test_y)

    """
    
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

def train_process(X,Y):
    x_train, y_train , x_test, y_test =  train_test_split(X,Y,test_size=0.1)
 # 生成模型，并喂入数据
    clf = LogisticRegression()
    clf.fit(x_train, y_train)
 # 保存模型（用joblib，不用pickle）
    joblib.dump(clf,"lr.model")    #from sklearn.externals import joblib
 #加载模型是： clf = joblib.load("lr.model")
 
 
 #6. 预测结果，并评测
    y_pred = clf.predict(x_test)  #预测出来的值计做y_pred
    y_true = y_test               #真实值计做y_true，和sklearn参数一模一样 
    target_names = ['class 0', 'class 1']
    print(classification_report(y_true, y_pred, target_names=target_names)) #可以参考sklearn官网API
    print(confusion_matrix(y_true, y_pred)) #混淆矩阵（记住！sklearn定义的混淆矩阵m行n列含义是：该样本真实值是m，预测值是n）
    print("precision_score:", precision_score(y_test,y_pred)) #打印精确率（记住！默认是positive，即标注为1的精确率）

    return y_pred,y_true
def plot_result(y_pred,y_true):
    #神秘代码，主要是保证plt字体显示正确
    plt.rcParams['font.sans-serif'] = ['SimHei']   
    plt.rcParams['font.family']='sans-serif' 
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(y_pred,"b.", label = "y_pred")   #blue，点号
    plt.plot(y_true,"r*", label = "y_true")   #red，星号
    plt.legend()
    plt.show()  #画的比较简略，可以进一步美化

path = 'D:\\zyh\\_workspace\\IOT_data\\logs3days'

slice_time_point(
             load_merge(
                 path
                 ))

""" plot_result(
    train_process(
        slice_time_point(
             load_merge(
                 path
                 )))) """

""" class data(self)：
        train = { 'X' : , 'Y' : }
        test = { 'X' : , 'Y' :  }
 """
