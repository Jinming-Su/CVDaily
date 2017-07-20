# 从神经网络到深度学习
### 什么是神经网络
在计算机科学中，通常所说的神经网络指人工神经网络(ANN).

先看一种简单的数学模型: 
![1](http://i2.kiimg.com/589172/c34cce4d943cf55f.png)  
输入: [x1, x2]  
参数: [w1, w2]
输出: [y]  
```
y = x1w1 + x2w2
```

为了模拟生物神经元，由于生物神经元本身达到一定刺激之后才能激活，因此在人工神经元中通过为神经元添加阈值进行激活，最简单的神经网络模型如下:  
![1](http://i1.buimg.com/589172/616840bfe7476c3f.png)
输入: [x1, x2]
参数: [w1, w2, b]
输出: [0, 1]
```
output = 0, x1w1 + x2w2 - b <= 0
		 1, x1w1 + x2w2 - b > 0
```
这个地方通常是转化为一个平滑的函数来表示，如sigmoid，relu等.  

很容易扩展到多层神经网络:
![1](http://i4.piimg.com/589172/0ba47c2adacdf9a8.png)  
已经证明的一个事实: 神经网络可以用来近似任何函数。  

### 神经网络求解实际问题
对于实际场景中的很多问题，例如根据色泽(青绿、乌黑、浅白)和敲声（浊响、沉闷、清脆）来判断一个瓜的好坏（好瓜坏瓜），并且已经知道了一些数据（比如一百组数据）:  
![1](http://i4.piimg.com/589172/691ccba889ee8ed7.png)  
然后来了一组新的数据，比如[青绿，清脆]来判断一个瓜是好瓜还是坏瓜。这种问题可以通过神经网络进行解决，模型如下:  
![1](http://i2.kiimg.com/589172/fc10412f2f17a8fc.png)  

### 求解神经网络
建立好模型之后，就要对以上模型进行求解。  
求解过程需要先构建一个代价函数（损失函数或目标函数），然后通过最小化或者最大化这个函数来对以上问题进行优化（优化问题）。一般使用梯度下降算法。

### 编程实现神经网络
基于tensorflow的代码
```
def weight_variable(shape):
    init = tf.random_normal(shape)
    return tf.Variable(init)

def bias_variable(shape):
    init = tf.constant(0.1, shape=shape)
    return tf.Variable(init)
   
W_fc1 = weight_variable([input_num, 16])
b_fc1 = bias_variable([16])
y_fc1 = tf.nn.relu(tf.matmul(x, W_fc1) + b_fc1)

W_fc2 = weight_variable([4, 8])
b_fc2 = bias_variable([8])
y_fc2 = tf.nn.relu(tf.matmul(y_fc1, W_fc2) + b_fc2)

cross_entropy = -tf.reduce_sum(yt * tf.log(y_fc2))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
```

### 深度学习与深度神经网络
当神经网络模型的网络层数比较多时，认为网络模型是深度神经网络。针对深度神经网络研究出了许多新的结构和方法，这些方法通常被称为深度学习方法。但是深度学习不只包括深度神经网络的相关方法，还包括诸如深度森林等方法。

### 深度学习比较火的领域
* 计算机视觉(Computer, CV): 包括图像识别、目标检测、语义分割等
* 语音识别
* 文本处理

### 框架排名
* tensorflow: 通用机器学习框架，几乎所有机器学习算法都可以进行实现，包括深度学习
* caffe: 深度学习框架鼻祖，主要针对卷积神经网络，主要应用领域为计算机视觉
* keras: 高度模块化，基于tensorflow或者theano
