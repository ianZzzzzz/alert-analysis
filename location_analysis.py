import pandas as pd
import matplotlib.pyplot as plt
file_name = '24.log'
data_names = ["1-ID","2-时间","3-1级区域","4-2级区域","5-3级区域","6-4级区域","7-温度过高","8-温度预警","15-箱门告警","16-防雷告警",
"18-风扇故障","19-网络设备异常","20-视频1网络异常","21-补光灯异常开启","22-补光灯异常关闭","23-视频2网络异常","24-视频3网络异常",
"25-视频4网络异常","26-视频5网络异常","27-视频6网络异常","28-温度低","29-监控网络连接异常","30-市电异常","longtitude","magtitude"]

singal_area_log = pd.read_csv(file_name, sep=",",header=None, names=data_names, encoding="gb2312")

df_gps_data = singal_area_log[["1-ID","longtitude","magtitude"]]

df_gps_base_id = df_gps_data.drop_duplicates("1-ID")

useful_gps_data = df_gps_base_id[df_gps_base_id["longtitude"]>113]

nomolization_gps_data = useful_gps_data

#nomolization_gps_data["longtitude"].apply(lambda x: x-113 )
#nomolization_gps_data["magtitude"].apply(lambda x: x-22 )
#print(nomolization_gps_data)
nomolization_gps_data.plot.scatter(x= "longtitude",y="magtitude" )
plt.show()