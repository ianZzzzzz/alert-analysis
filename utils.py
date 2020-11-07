'''INSTRUCTION:  The function of this code is to classify
the alarm data then remove the unalarm rows,
finally output the data as csv file in chronological order.'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def find_all_file(folder_name):

    for root,ds,fs in os.walk(folder_name):
        for f in fs :
            full_name = os.path.join(root,f)
            yield full_name


def tital_save_close_fig_excel(data, name, fig_suffix='.png', excel_suffix='.csv'):
    sns.heatmap(data, cmap='Reds', vmax=1, vmin=-1, center=0)
    plt.title(name)
    plt.savefig(name + fig_suffix)
    plt.close("all")  # 不清理会导致图例在下一张图重复
    data.to_csv(name + excel_suffix, encoding='utf_8_sig')


def wash_useless_row_and_rewrite():
    BASIC_FILE_PATH = 'E:/data/program_1/rewrite3/'
    files = os.listdir(BASIC_FILE_PATH)  # get file path
    files.sort(key=lambda x: int(x[4:-4]))  # sorting by file number       :-4 blocking '.csv'
    networkERROR = pd.DataFrame()
    electricSupplyALERT = pd.DataFrame()
    anti_ThunderALERT = pd.DataFrame()
    fanERROR = pd.DataFrame()
    doorALERT = pd.DataFrame()
    for filename in files:
        path = BASIC_FILE_PATH + filename  # path+name
        frame1 = pd.read_csv(path, sep=',', encoding='gbk', index_col=0)  # read
        columns_basic = ['2-时间', 'date_time', '3-1级区域', '4-2级区域', '44-经度', '45-维度', '1-ID']

        networkERROR = networkERROR.append(
            frame1[
                columns_basic + ['19-网络设备异常', '29-监控网络连接异常', '20-视频1网络异常', '23-视频2网络异常', '24-视频3网络异常']
                ],
            ignore_index=True
        )
        electricSupplyALERT = electricSupplyALERT.append(frame1[columns_basic + ['30-市电异常']], ignore_index=True)
        anti_ThunderALERT = anti_ThunderALERT.append(frame1[columns_basic + ['16-防雷告警']], ignore_index=True)
        fanERROR = fanERROR.append(frame1[columns_basic + ['18-风扇故障']], ignore_index=True)
        doorALERT = doorALERT.append(frame1[columns_basic + ['15-箱门告警']], ignore_index=True)

    ''' ALL_ERROR_data = ALL_ERROR_data.append(
        frame1[
            columns_basic+['30-市电异常','15-箱门告警','16-防雷告警','18-风扇故障', '19-网络设备异常','29-监控网络连接异常','20-视频1网络异常','23-视频2网络异常','24-视频3网络异常']],
            ignore_index=True
        )
    '''

    networkERROR['汇总'] = networkERROR['19-网络设备异常'] + networkERROR['29-监控网络连接异常'] + networkERROR['20-视频1网络异常'] + \
                         networkERROR['23-视频2网络异常'] + networkERROR['24-视频3网络异常']
    # filter
    networkERROR = networkERROR[networkERROR['汇总'].isin([1])]
    electricSupplyALERT = electricSupplyALERT[electricSupplyALERT['30-市电异常'].isin([1])]
    anti_ThunderALERT = anti_ThunderALERT[anti_ThunderALERT['16-防雷告警'].isin([1])]
    fanERROR = fanERROR[fanERROR['18-风扇故障'].isin([1])]
    doorALERT = doorALERT[doorALERT['15-箱门告警'].isin([1])]
    # sort by time+date
    net = networkERROR.sort_values(by="2-时间")
    ele = electricSupplyALERT.sort_values(by="2-时间")
    thu = anti_ThunderALERT.sort_values(by="2-时间")
    fan = fanERROR.sort_values(by="2-时间")
    door = doorALERT.sort_values(by="2-时间")

    # write
    net.to_csv(BASIC_FILE_PATH + 'networkERROR.csv', sep=',', encoding='gbk')
    ele.to_csv(BASIC_FILE_PATH + 'electricSupplyALERT.csv', sep=',', encoding='gbk')
    thu.to_csv(BASIC_FILE_PATH + 'anti_ThunderALERT.csv', sep=',', encoding='gbk')
    fan.to_csv(BASIC_FILE_PATH + 'fanERROR.csv', sep=',', encoding='gbk')
    door.to_csv(BASIC_FILE_PATH + 'doorALERT.csv', sep=',', encoding='gbk')
