#numpy读取数据

    CSV:Comma-Separated Value,逗号分隔值文件
    显示：表格状态
    源文件：换行和逗号分隔行列的格式化文本,每一行的数据表示一条记录
    
    np.loadtxt(fname,dtype=np.float,delimiter=None,skiprows=0,usecols=None,unpack=False)
<br>

|参数|解释|
|---|---|
|frame|文件、字符串或产生器，可以是.gz或bz2压缩文件|
|dtype|数据类型，可选，CSV的字符串以什么数据类型读入数组中，默认np.float|
|delimiter|分隔字符串，默认是任何空格，改为 逗号|
|skiprows|跳过前x行，一半跳过第一行表头|
|usecols|读取指定的列，索引，元组类型|
|unpack|如果True，读入属性将分别写入不同数据变量，False读入数据只写入一个数组变量<br>，默认False

#numpy中数组的拼接
    np.vstack((t1,t2)) ————>竖直拼接
    np.hstack((t1,t2)) ————>水平拼接

#numpy的行列交换
    交换列
    t1[:,[0,1]] = t1[:,[1,0]]
    
    交换行
    t1[[0,1],:] = t1[[1,0],:]    
#numpy中好用的方法有:
    
    获取最大值最小值的位置
    np.argmax(t,axis=0)
    np.argmin(t,axis=1)
    创建一个全0的数组: np.zeros((3,4))
    创建一个全1的数组:np.ones((3,4))    
    创建一个对角线为1的正方形数组(方阵)：np.eye(3)

#numpy生成随机数

|参数|解释|
|---|---|
|.rand(d0,d1,..dn)|创建d0-dn维度的均匀分布的随机数组，浮点数，范围从0-1|
|.randn(d0,d1,..,dn)|创建d0-dn维度的标准正态分布随机数，浮点数，平均数0，标准差1|
|.randint(low,high,(shape))|给定上下限范围选取随机数整数，范围是low，high，形状是shape|
|.uniform(low,high,(size))|产生具有均匀分布的数组，low起始值，high结束值，size形状|
|.normal(loc,scale,(size))|从指定正太分布中随机抽取样本，分布中心是loc（概率分布的均值），<br>标准差是scale，形状是size|
|.seed(s)|随机数种子，s是给定的种子值。因为计算机生成的是伪随机数，<br>所以通过设定相同的随机数种子，可以生成相同的随机数

#numpy中的nan和inf
    
#####nan(NAN,Nan):not a number表示不是一个数字

    什么时候numpy中会出现nan：
          当我们读取本地的文件为float的时候，如果有缺失，就会出现nan
          当做了一个不合适的计算的时候(比如无穷大(inf)减去无穷大)
    
    inf(-inf,inf):infinity,inf表示正无穷，-inf表示负无穷
    
    什么时候回出现inf包括（-inf，+inf）
          比如一个数字除以0，（python中直接会报错，numpy中是一个inf或者-inf）

#####nan的注意点：
1. 两个 nan 是不相等的
2. np.nan!=np.nan
3. 如何判断一个数字是否为nan呢？
    * 通过np.isnan(a)来判断，返回bool类型，例如把nan换成0：
        * array[1, 2, nan]
        *t[np.isnan(t)]=0
4. nan 和任何值计算都为nan
5. 如何判断nan的个数？
    * np.count_nonzero(t!=t)
    * 其中np.count_nonzero()是用来统计数组中不为0的个数
    * 因为nan!=nan 所以由此可以判断出来
6. 所以当出现 nan 的时候如何做呢？
    * 一般的方式是：把缺失的数值替换为均值（中值）或者直接删除缺失值的一行

##如何计算一组数据的中值或者是均值？
    求和： t.sum(axis=None)
    均值： t.mean(a,axis=None)  受离群点的影响较大
    中值： np.median(t,axis=None) 
    最大值： t.max(axis=None) 
    最小值： t.min(axis=None)
    极值： np.ptp(t,axis=None) 即最大值和最小值只差
    标准差： t.std(axis=None) 
        标准差是一组数据平均值分散程度的一种度量。
        一个较大的标准差，代表大部分数值和其平均值之间差异较大；
        一个较小的标准差，代表这些数值较接近平均值
        反映出数据的波动稳定情况，越大表示波动越大，约不稳定




###拓  展
#####如何实现对数组的转置
    使用 transpose ；T；swapaxes 等方法，即 行变列，列变行
