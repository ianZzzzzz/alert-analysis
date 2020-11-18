# multi output multi step model LSTM
# TODO PCA
import numpy as np
import pandas as pd 
import utils
def find_useful_id(raw_data,key,value):
    data = raw_data

    data_name = list([ "id","time","area3","area4","area5","6-4级区域",'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','v','c','','','tem',"longtitude","magtitude" ] 
    )
    data.columns = data_name
  
    df = data.drop(columns = ['v','c','tem',"area3","area4","area5","6-4级区域","longtitude","magtitude"])
    

    df = df.groupby(key).sum() # 进行这一步时 id列已经作为index了

    # df.set_index(['id'],inplace = True)

    df = df.sum(axis = 1) # 求各id 的总告警数量
    
    useful_id = df[df>value].index.values # int64 array

    return useful_id
    
path = ''
raw_data = utils.load_merge(path)
id_list = find_useful_id(raw_data,key = 'id',value = 10)

def find_useful_log(raw_data,key,value_list):

    raw_data.columns = list([''])
    raw_gb_key = raw_data.groupby(key)
    raw_gb_key = dict(list(raw_gb_key))
    for i in value_list :
        if i in raw_gb_key:
            raw_gb_key[i] = raw_gb_key[i].drop(columns = key )

            # 做插值

