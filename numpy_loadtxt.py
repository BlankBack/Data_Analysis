
"""
那么,结合之前的所学的matplotlib把英国和美国的数据呈现出来?

看到这个问题,我们应该考虑什么?
我们想要反映出什么样的结果,解决什么问题?
选择什么样的呈现方式?
数据还需要做什么样的处理?
写代码

"""
import numpy as np

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"


t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int")
t2 = np.loadtxt(us_file_path, delimiter=",",dtype="int")

print(t2)
print('*' * 100)

# # 取行
# print(t2[2])
# print('*' * 100)

# 取连续的多行
# print(t2[2:])

# 取不连续的多行
# print(t2[[2,8,10]])

# 取行
# print(t2[1,:])
# print(t2[2:,:])
# print(t2[[2,10,3],:])

# 取列
# print(t2[:,[0]])
# print(t2[:,[2]])
# 取不连续多列
# print(t2[:,[0,2]])
# 取连续的多列
# print(t2[:,1:])

# 取多行多列的值，例如：第三行，第四列的值
# print(t2[[2],[3]])
# a = t2[2,3]
# print(type(a))

# 取第三行到第五行，第2列到第4列的值
# b = t2[2:4,1:3]
# print(b)

# 取多个不相邻的点
# 选出来的结果是（0,0）（2,1）（2,3）
# c = t2[[0,2,2],[0,1,3]]
# print(c)

# # 修改数组中的值
# t3 = np.arange(24).reshape(4,6)
# print(t3)
# print('*' * 100)
# # # 该操作为numpy中的布尔索引
# # t2[t2<10] = 3
# # print(t2)
#
# # 运用三元运算符进行修改
# # d = np.where(t2>10,0,10)
# # print(d)
#
# # numpy 中的裁剪操作clip
# e = t3.clip(10,18)
# print(e)













