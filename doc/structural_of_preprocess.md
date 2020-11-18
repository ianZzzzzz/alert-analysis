# filter 
    1 对id进行gb.sum 对总告警小于10 的设备舍弃 
        2 再统计余下设备在各区域的分布 舍弃无数据的区域
            3 对余下设备的log数据进行时间上的插值 一分钟重采样
                4 


# tree 
    class load : 
        
        raw = []
        def __init__(self,folder_path):
            
            self.raw = load_merge(folder_path)
            
            def load_merge(folder_path):

                def return_file_path(path):
                    for root,ds,fs in os.walk(folder_name):
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

            
                

    #   def find(raw,key,value)
            sclice
            groupby key
    #    export :path ,key
    data = Data(path)

    for node in tree:
        id_list = data.find(key = 'level_1',value = node,return_info = 'id')
        for id in id_list :
            tree.create_node(id,id,parent = node,data=[])


        

        

    



