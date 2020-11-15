import pandas as pd
import numpy as np
#类定义
class log_of_area:
    #定义基本属性
    path = ''
    
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,path):
        self.path = path  
        
    
    def concat (self,path):
        

        

class log_of_area_list:
    data = []

    def __init__(self, data=[]):
        self.data = data
    
    def append_log_of_area(self,log_of_area):
        self.data.append(log_of_area)

        """ area数据形式未定义 该函数待定
            def group_by_area(self):
            self.data = self.data.groupby()
            return
        """
    def groupById(self):
        return
    
    def getTimeBetween():
        return

    def pluckDataBy(key, chunck):
        return


# 实例化类
raw = pd.read_csv('D:\\zyh\\_workspace\\IOT_data\\logs3days\\portal14.csv')
p = log_of_area(path)

print( p.id.shape,p.time)