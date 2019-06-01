
import numpy as np

"""
如何计算一组数据中的中值或者是均值？
如何删除有缺失数据的哪一行？
求和：t.sum(axis=None)
均值：t.mean(a,axis=None)  受离群点的影响较大
中值：np.median(t,axis=None) 
最大值：t.max(axis=None) 
最小值：t.min(axis=None)
极值：np.ptp(t,axis=None) 即最大值和最小值只差
标准差：t.std(axis=None) 

"""

t1 = np.arange(24).reshape(4,6)
t1 = t1.astype(float)
t1[3,3] = np.nan
print(t1)

# 求和函数
print("该数组的和",t1.sum())
print("行求和",t1.sum(axis=1))
print("列求和",t1.sum(axis=0))

# 求均值
print("均值为",t1.mean())
print("每一列均值为",t1.mean(axis=0))
print("每一行均值为",t1.mean(axis=1))

# 求中值

print("每一列中值为：",np.median(t1,axis=0))
print("每一行中值为：",np.median(t1,axis=1))

# 最大值和最小值
print("每一列最大/小值为：\n",t1.max(axis=0),t1.min(axis=0))
print("每一行最大/小值为：\n",t1.max(axis=1),t1.min(axis=1))

# 极值
print("极值：\n", t1.ptp(axis=0), '\n', t1.ptp(axis=1))

# 标准差
print("标准差：", t1.std(axis=1), '\n', t1.std(axis=0)),