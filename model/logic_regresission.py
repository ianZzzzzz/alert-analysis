import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from . import utils
from sklearn.model_selection import train_test_split  # 这里是引用了交叉验证
from sklearn.linear_model import LinearRegression  # 线性回归


utils.wash_useless_row_and_rewrite()

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

df_label = pd.read_csv('labels.csv', sep=',')
df_area = pd.read_csv("area.csv", sep=',')

columns = df_label.iloc[0, :].__len__()

df_label_copy = df_label.iloc[:, 3:columns]
columns = df_area.iloc[0, :].__len__()
df_area_copy = df_area.iloc[:, 1:columns]

df_area_clean = df_area_copy.drop(columns='@51')  # 51无数据

# 相关性检验=====================================================================================
utils.tital_save_close_fig_excel(data=df_label_copy.corr(), name="告警类型间的Pearson相关系数")
utils.tital_save_close_fig_excel(data=df_label_copy.corr("spearman"), name="告警类型间的Spearman相关系数")
utils.tital_save_close_fig_excel(data=df_area_clean.corr(), name="各区域告警数据间的Pearson相关系数")
utils.tital_save_close_fig_excel(data=df_area_clean.corr("spearman"), name="各区域告警数据间的Spearman相关系数")

# 线性回归========================================================
sns.pairplot(
    df_label_copy,
    x_vars=['箱门告警', '防雷告警'],
    y_vars='风扇故障',
    kind='reg',
    size=5,
    aspect=0.7,
)
# plt.show()
pd_data = df_label_copy


def mul_lr(x1, x2, y):
    x_value = pd_data.loc[:, (x1, x2)]
    y_value = pd_data.loc[:, y]
    x_train, x_test, y_train, y_test = train_test_split(x_value, y_value, test_size=0.2, random_state=100)
    print('x_train.shape={}\n y_train.shape ={}\n x_test.shape={}\n,  y_test.shape={}'
          .format(x_train.shape, y_train.shape, x_test.shape, y_test.shape))
    linear_regression = LinearRegression()
    model = linear_regression.fit(x_train, y_train)
    print(model)
    # 训练后模型截距
    print("自变量：{},{}  因变量：{}".format(x1, x2, y))
    print("截距B= {}".format(linear_regression.intercept_))
    # 训练后模型权重（特征个数无变化）
    # print("参数：{}".format(linear_regression.coef_))

    feature_cols = ['箱门告警', '防雷告警', '风扇故障']
    matrix = list(zip(feature_cols, linear_regression.coef_))
    print(matrix)

    # 预测

    linear_regression_predict = linear_regression.predict(x_test)
    #  print(linear_regression_predict) #10个变量的预测结果
    # 评价
    # (1) 评价测度
    # 对于分类问题，评价测度是准确率，但这种方法不适用于回归问题。我们使用针对连续数值的评价测度(evaluation metrics)。
    # 介绍3种常用的针对线性回归的测度。
    # 1)平均绝对误差(Mean Absolute Error, MAE)
    # (2)均方误差(Mean Squared Error, MSE)
    # (3)均方根误差(Root Mean Squared Error, RMSE)
    # 这里我使用RMSE。
    sum_mean = 0
    for i in range(len(linear_regression_predict)):
        sum_mean += (linear_regression_predict[i] - y_test.values[i]) ** 2
    sum_error = np.sqrt(sum_mean / 100)  # 这个100是你测试级的数量
    # calculate RMSE by hand
    print("RMSE by hand:", sum_error)
    # 做ROC曲线
    plt.figure()
    plt.plot(range(len(linear_regression_predict)), y_test, 'r', label="真实值")
    plt.plot(range(len(linear_regression_predict)), linear_regression_predict, 'b', label="预测值")
    plt.title("自变量" + x1 + x2 + "\n因变量" + y)
    plt.legend(loc="upper right")  # 显示图中的标签
    plt.xlabel("自变量")
    plt.ylabel('因变量')
    plt.show()


mul_lr(x1='箱门告警', x2='防雷告警', y='风扇故障')
mul_lr(x1='箱门告警', x2='风扇故障', y='防雷告警')
mul_lr(x1='风扇故障', x2='防雷告警', y='箱门告警')
