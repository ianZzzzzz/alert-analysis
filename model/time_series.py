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

    
    raw_data.columns = list([
         "id","time","level_1","level_2",
         "5","6",'high_temperature','temperature_alam',
         '9','10','11','12',
         '13','14','door_alarm','lightning_alarm',
         '17','fan_failure','network_device_error','v1_net_error',
         '21','22','v2_net_error','v3_net_error',
         'v4_net_error','26','27','28',
         'monintoring_net_connect_err','power_supply_err','31','32',
         '33','34','35','36',
         '37','38','voltage','current',
         'power','42','temperature',"longtitude","magtitude" ] 
    )

    """   保留以备导出
    raw_data = raw_data[[ 
        "id","time", 

        "level_1","level_2","longtitude","magtitude", # location
        'door_alarm', 'fan_failure','network_device_error', # device
        'high_temperature','temperature_alam','temperature', # temperature
        'lightning_alarm','power_supply_err','voltage','current', # power/electric

        'v1_net_error','v2_net_error','v3_net_error','v4_net_error',  # network
        'monintoring_net_connect_err' # network 
        ]]
    """


    raw_data = raw_data[[ 
        "id","time", 

        "level_1","level_2","longtitude","magtitude", # location
        'door_alarm', 'fan_failure','network_device_error', # device
        'high_temperature','temperature_alam','temperature', # temperature
        'lightning_alarm','power_supply_err','voltage','current', # power/electric

        'v1_net_error','v2_net_error','v3_net_error','v4_net_error',  # network
        'monintoring_net_connect_err' # network 
        ]]# 保留以备导出

    raw_gb_key = raw_data.groupby(key)
    raw_gb_key = dict(list(raw_gb_key))
    for i in value_list :
        if i in raw_gb_key:
            raw_gb_key[i] = raw_gb_key[i].drop(columns = key )

            # 做插值

