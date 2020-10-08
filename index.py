import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def tital_save_close_fig_excel(data,name,fig_tail,excel_tail):
    sns.heatmap(data, cmap='Reds', vmax=1, vmin=-1, center=0)
    plt.title(name)
    plt.savefig(name + fig_tail)
    plt.close("all")  # 不清理会导致图例在下一张图重复
    data.to_csv(name+excel_tail,encoding='utf_8_sig')

plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

excel_tail='.csv'
fig_tail='.png'

df_label = pd.read_csv('labels.csv', sep=',')
df_area=pd.read_csv("area.csv",sep=',')

columns = df_label.iloc[0, :].__len__()

df_label_copy = df_label.iloc[:, 3:columns]
columns = df_area.iloc[0, :].__len__()
df_area_copy = df_area.iloc[:, 1:columns]

df_area_clean = df_area_copy.drop(columns='@51') #51无数据

# 相关性检验=====================================================================================
tital_save_close_fig_excel(data=df_label_copy.corr(),
                           name="告警类型间的Pearson相关系数",
                           fig_tail=fig_tail,
                           excel_tail=excel_tail)

tital_save_close_fig_excel(data=df_label_copy.corr("spearman"),
                           name="告警类型间的Spearman相关系数",
                           fig_tail=fig_tail,
                           excel_tail=excel_tail)

tital_save_close_fig_excel(data=df_area_clean.corr(),
                           name="各区域告警数据间的Pearson相关系数",
                           fig_tail=fig_tail,
                           excel_tail=excel_tail)


tital_save_close_fig_excel(data=df_area_clean.corr("spearman"),
                           name="各区域告警数据间的Spearman相关系数",
                           fig_tail=fig_tail,
                           excel_tail=excel_tail)


# 线性回归========================================================


from sklearn.model_selection import train_test_split #这里是引用了交叉验证
from sklearn.linear_model import LinearRegression  #线性回归
from sklearn import metrics
import numpy as np


sns.pairplot(df_label_copy,
             x_vars=['箱门告警','防雷告警'],
             y_vars='风扇故障',
             kind='reg',
             size=5,
             aspect=0.7,
             )
#plt.show()
pd_data=df_label_copy
def mul_lr(X1,X2,Y):
    x = pd_data.loc[:,(X1,X2)]
    y = pd_data.loc[:,Y]
    X_train,X_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state=100)
    print('X_train.shape={}\n y_train.shape ={}\n X_test.shape={}\n,  y_test.shape={}'
          .format(X_train.shape,y_train.shape, X_test.shape,y_test.shape))
    linreg = LinearRegression()
    model=linreg.fit(X_train, y_train)
    print (model)
    # 训练后模型截距
    print("自变量：{},{}  因变量：{}".format(X1,X2,Y))
    print ("截距B= {}".format(linreg.intercept_))
    # 训练后模型权重（特征个数无变化）
   # print("参数：{}".format(linreg.coef_))

    feature_cols = ['箱门告警','防雷告警','风扇故障']
    B=list(zip(feature_cols,linreg.coef_))
    print(B)

# 预测

    y_pred = linreg.predict(X_test)
  #  print(y_pred) #10个变量的预测结果
# 评价
    # (1) 评价测度
    # 对于分类问题，评价测度是准确率，但这种方法不适用于回归问题。我们使用针对连续数值的评价测度(evaluation metrics)。
    # 介绍3种常用的针对线性回归的测度。
    # 1)平均绝对误差(Mean Absolute Error, MAE)
    # (2)均方误差(Mean Squared Error, MSE)
    # (3)均方根误差(Root Mean Squared Error, RMSE)
    # 这里我使用RMES。
    sum_mean=0
    for i in range(len(y_pred)):
        sum_mean+=(y_pred[i]-y_test.values[i])**2
    sum_erro=np.sqrt(sum_mean/100)  #这个10是你测试级的数量
    # calculate RMSE by hand
    print ("RMSE by hand:",sum_erro)
    #做ROC曲线
    plt.figure()
    plt.plot(range(len(y_pred)), y_test, 'r', label="真实值")
    plt.plot(range(len(y_pred)),y_pred,'b',label="预测值")
    plt.title("自变量"+X1+X2+"\n因变量"+Y)
    plt.legend(loc="upper right") #显示图中的标签
    plt.xlabel("自变量")
    plt.ylabel('因变量')
    plt.show()


mul_lr(X1='箱门告警',X2='防雷告警',Y='风扇故障')
mul_lr(X1='箱门告警',X2='风扇故障',Y='防雷告警')
mul_lr(X1='风扇故障',X2='防雷告警',Y='箱门告警')
