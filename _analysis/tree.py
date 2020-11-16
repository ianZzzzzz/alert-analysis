import treelib
from treelib import Tree, Node
import os
import pandas as pd
import numpy as np
def tree():
    t = Tree ()
    t.create_node(0,0,data = [])
    # 0
    a0 = [15,16,17,55,69,70,71]
    for i in a0 :
        t.create_node(i,i,parent = 0,data=[])

    # 15

    a15 = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 72]
    for i in a15:
        t.create_node(i,i,parent = 15,data=[])

    # 16
    for i in range(31,55):
        t.create_node(i,i,parent = 16,data=[])

    t.show()
    return


class load : 
    
    raw = np.ndarray([])
    
    def __init__(self,folder_path):
        
        column = 0
        row = 0
        def load_merge(folder_path):

            def return_file_path(path):
                for root,ds,fs in os.walk(path):
                    for f in fs :
                        full_path = os.path.join(root,f)
                        yield full_path

            file_list = return_file_path(folder_path) # get file path
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
            return data_frame.values


        self.raw = load_merge(folder_path)
    
    def choose_column(self,column):
        
        data = self.raw[:,column]
        return data
    
        
path = 'D:\\zyh\\_workspace\\IOT_data\\abnormal_data'

data = load(path)  
print(data.choose_column(column = 1))