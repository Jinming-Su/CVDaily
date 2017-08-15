### 卷积是什么
* 卷积操作是一种数学操作  
![1](http://i1.bvimg.com/589172/2a464f2366c1bda1.png)   
* 图像领域的深度学习之所以选择使用卷积结构，主要是因为卷积操作能够有效模拟人类视觉大脑皮层的局部感受野，深度卷积神经网络能够模拟人类大脑皮层细胞的层次结构

### Caffe是什么
* Caffe是一个深度学习框架，全称是Convolutional Architecture for Fast Feature Embedding，注意是 ***卷积框架***
* 作者: 贾扬清
* 论文: 
Caffe: Convolutional Architecture for Fast Feature Embedding 
* 源代码: https://github.com/BVLC/caffe
* 优点
	* C++实现，速度快
	* 支持GPU加速
	* 开源，模块化设计，网状层级结构
	* 文档齐全
	* 提供了命令行、Matlab和Python接口
	* 尤其适合图片特征提取
* 缺点
	* 一般认为只支持CNN，不支持RNN等
	* 适用的场景主要面向计算机视觉，对于语音识别等支持较少
	* 依赖包多，ProtoBuffer、gflags、glog、blas、hdf5、opencv等

### Caffe能做什么
* 能够很简单地进行卷积操作，能够很简单地实现卷积神经网络模型
* 举例: 一种经典的手写字识别的卷积神经网络模型LeNet，只需要使用protobuffer格式定义即可使用
![1](http://i1.bvimg.com/589172/1b046671ce750f71.png)  
代码如下:  
```
// deploy.prototxt
name: "LeNet"
layer {
  name: "data"
  type: "Input"
  top: "data"
  input_param { shape: { dim: 64 dim: 1 dim: 28 dim: 28 } }
}
layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"
  top: "conv1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 20
    kernel_size: 5
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool1"
  type: "Pooling"
  bottom: "conv1"
  top: "pool1"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "conv2"
  type: "Convolution"
  bottom: "pool1"
  top: "conv2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 50
    kernel_size: 5
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool2"
  type: "Pooling"
  bottom: "conv2"
  top: "pool2"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "ip1"
  type: "InnerProduct"
  bottom: "pool2"
  top: "ip1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 500
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu1"
  type: "ReLU"
  bottom: "ip1"
  top: "ip1"
}
layer {
  name: "ip2"
  type: "InnerProduct"
  bottom: "ip1"
  top: "ip2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 10
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "prob"
  type: "Softmax"
  bottom: "ip2"
  top: "prob"
}
```  

### 如何使用Caffe
#### 安装
* Caffe是开源的深度学习框架，代码托管在github上，https://github.com/BVLC/caffe  
* 安装教程: http://blog.csdn.net/u014451076/article/details/74629403

#### 使用
* protoBuffer
protoBuffer是一种轻便高效的结构化数据存储格式  
* train.prototxt
Caffe中神经网络模型的定义文件
* solver.prototxt
Caffe中神经网络模型求解器配置文件，配置模型的求解策略  
```
// solver.prototxt
net: "examples/mnist/lenet_train_test.prototxt"
test_iter: 100
test_interval: 500
base_lr: 0.01
momentum: 0.9
weight_decay: 0.0005
lr_policy: "inv"
gamma: 0.0001
power: 0.75
display: 100
max_iter: 10000
snapshot: 5000
snapshot_prefix: "examples/mnist/lenet"
solver_mode: GPU
```

### 举例
一个猫狗分类的例子  
* 源代码在这里: 链接: https://pan.baidu.com/s/1kVzc2ub 密码: tjqx
* 制作数据集，包括训练集和测试集，并将数据转化为lmdb，（求出均值）
* 编写网络模型文件train.prototxt，求解器文件solver.prototxt
* 编写训练脚本train.sh，进行训练
* 编写部署网络模型文件test.prototxt，编写部署脚本test.sh，进行部署  
**类似地，完成了这个例子之后，就可以通过更改数据集完成很多事物的分类，比如:  **
  * 车牌识别
  * 车型识别
  * 性别识别
  * 等等...可以自己尝试一下

### 完成以上例子，Caffe就算入门了，接下来要学习
* 深入理解Caffe代码，理解Caffe的工作机制，修改Caffe满足自己的工作要求
* 寻找适合自己的任务的网络模型
* 一些技巧：数据处理，网络优化，训练策略优化等...
