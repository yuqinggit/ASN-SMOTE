import numpy as np
import pandas as pd
from collections import Counter


# 数据处理
data = pd.read_excel('pima.xlsx')

#g_sample=generate_x(data,100,5)

print("ASN_SMOTE")

# axis=1表示操作是沿着列（特征）进行的。
# 原代码：X = data.drop(['DFS'],axis=1)
# 改：
X = data.drop(['Class'],axis=1)
Y = data['Class']
x=np.array(X)
y=np.array(Y)

print(sorted(Counter(y).items()))