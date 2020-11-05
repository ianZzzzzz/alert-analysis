
import pandas as pd 

raw_data_path='raw_data_path'
final_feature_path='final_feature_path'
frist_area = 1
last_area = 18
area_list = range(frist_area,last_area)
# load data
raw_data_df =pd.read_csv(raw_data_path, index_col='time', usecols='',)
# devide data
for area in area_list:
    singal_area_data_df = raw_data_df[raw_data_df['area']==area]
    resample_1min_sum_singal_area = singal_area_data_df.resample('1min').sum() # 这行的用法不一定对
    resample_1min_sum_singal_area.to_csv(area+".csv") # 还要做时间线补齐
    



