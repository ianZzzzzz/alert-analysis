# todo
    gps cluster
        从sklearn返回的onehot里取聚类标签
        给各个设备打上标签
    展示数据状况
        每台设备和每个区域的数据量
        基于数据量来确定在哪个层面上进行建模
            

#  解决思路
    特征的提取和识别交给深度学习
    人要解决的问题是缩小问题的范围

# 切入角度
    空间
        按照位置对设备ID进行聚类 训练时等比例抽取训练数据
            GPS
            区域结构表

# 模型 
    聚类
        GPS聚类图已经完成 在image/k_mean里
        
        
   
    多标签分类问题
```mermaid
    graph TB
        GPS_DATA -->k_mean-->labels
        device_history_data-->deep_model-->multi_label
        device_gps_data-->deep_model

        log_data-->设备过往告警汇总在一行-->device_history_data
    
 ```    
 
 