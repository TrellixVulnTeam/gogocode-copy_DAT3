import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 读取数据：
path = "url"
column_name = ["特征1", "特征2", "特征3"]
data = pd.read_csv(path, names=column_name)

# 缺失值处理
# 1.替换为np.nan
data = data.replace(to_replace="?", value=np.nan)

# 2.删除缺失样本
data.dropna(inplace=True)

# 筛选特征值和目标值
x = data.iloc[:, 1:-1]
y = data["Class"]

# 划分数据集
x_train, x_test, y_train, y_test = train_test_split(x, y)

# 标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 预估器
estimator = LogisticRegression()
estimator.fit(x_train, y_train)

# 逻辑回归的模型参数：回归系数和偏置
# estimator.coef_  是回归系数
# estimitor.intercept_ 是偏置

# 模型评估
# 方法1：直接对比真实值和预测值
y_predict = estimator.predict(x_test)
print("直接对比真实值和预测值：", y_test == y_predict)

# 方法2：计算准确率
score = estimator.score(x_test, y_test)
print("准确率为：", score)

# 查看精确率，召回率，F1-score
report = classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"])  # 2代表良性，4代表恶性
print(report)
