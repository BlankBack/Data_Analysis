
import numpy as np

# 数组的计算

t5 = np.arange(24).reshape((4,6))
print(t5)
print('*'*100)
print(t5+2)
print('*'*100)
print(t5*2)
print('*'*100)
print(t5/2)
print(t5/0)
"""
nan 不是一个数组，在numpy中用来专门表示0/0
inf 无限；无穷
"""


print('*'*100)
print(t5)
t6 =np.arange(100,124).reshape((4,6))
print(t6)
print(t6+t5)
print(t5*t6)

print('*'*100)
print(t5)
t7 = np.arange(0,6)
print(t5-t7)

print('*'*100)
t8 = np.arange(27).reshape((3,3,3))
print(t8)
t9 = np.arange(3).reshape((3,1))
print(t9)
print('*'*100)
print(t8*t9)

"""
在numpy中可以理解为方向,使用0,1,2...数字表示,对于一个一维数组,
只有一个0轴,对于2维数组(shape(2,2)),有0轴和1轴,对于三维数组(shape(2,2,3)),有0,1,2轴

"""
