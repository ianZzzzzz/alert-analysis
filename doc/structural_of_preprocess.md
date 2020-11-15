#```mermaid
    graph TB

#   class load : path
##       concat

#    find : raw,key,value
        sclice
        groupby key
#    export :path ,key
data = Data(path)
for i in level_1:

    id_in_level_1 = data.find(key = 'level_1',value = i,return_info = 'id')

    # create area level tree
    tree = Tree()

    for id in id_in_area_3:

        tree.create_node(tag=str(id), identifier=str(id), data=np_matrix)

#```
np.genfromtxt(("D:\\zyh\\_workspace\\IOT_data\\abnormal_data\\69_gps_all_zero.csv"), delimiter=",")

level_1_tree = Tree ()
for