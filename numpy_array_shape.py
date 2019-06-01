
import numpy as np

t1 = np.arange(12)

print(t1)

print(t1.shape)

t2 = np.array([[1,2,3],[4,5,6]])
print(t2)
print(t2.shape)

print('*'*50)

t3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(t3)
print(t3.shape)

print('*'*50)
t4 = np.arange(12)
print(t4)
print(t4.reshape(3,4))

print('*'*50)

t5 = np.arange(24).reshape((3,2,4))
print(t5)
print('*'*50)
print(t5.reshape(4,6))
print(t5.reshape(24,1))
print(t5.reshape(1,24))

print('*'*50)

t6 = t5.reshape((t5.shape[0]*t5.shape[1]*t5.shape[2]))
print(t6)

print(t5.flatten())