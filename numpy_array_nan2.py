
import numpy as np



def fill_ndarray(t1):
    for i in range(t1.shape[1]):    #shape[0]为行数，shape[1]为列数
        temp_col = t1[:,i]  #当前的一列
        nan_nums = np.count_nonzero(temp_col!=temp_col)
        if nan_nums !=0:    #不为0，说明当前这一列中有nan
            temp_not_nun_col = temp_col[temp_col==temp_col]     # 当前一列不为nan的array
            temp_not_nun_col.mean()

            # 选中当前为nan的位置，把值赋值为不为nan的均值
            temp_col[np.isnan(temp_col)] = temp_not_nun_col.mean()
    return t1

if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype(float)
    print(t1)

    print("将t1的第二行中第三列以后的所有数值变为nan：")
    t1[1, 2:] = np.nan
    print("包含nan的数组:\n",t1)
    t1 = fill_ndarray(t1)
    print("修改nan值后的数组:\n",t1)