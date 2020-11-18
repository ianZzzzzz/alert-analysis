import numpy as np
import pandas as pd 

def filter(raw_data):
    data = raw_data

    data_name = list([ "id","time","area3","area4","area5","6-4级区域",'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','v','c','','','tem',"longtitude","magtitude" ] 
    )
    data.columns = data_name
  
    df = df.drop(columns = ['v','c','tem',"area3","area4","area5","6-4级区域","longtitude","magtitude"])
    

    df = df.groupby('id').sum() #dfg

    
    df = df.sum(axis = 1) # 求各id 的总告警数量
    
    useful_id = df[df>10].index 
    