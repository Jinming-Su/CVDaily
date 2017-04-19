---
title: 【BN】Batch Normalization:Accelerating Deep Network Training by Reducing Internal Covariate Shift笔记
date: 2017-04-14 00:00:01
categories:
- Deep_Learning
- Paper
tags:
- batchnormalization
description: Batch Normalization
---

### 基本情况
* time: 2015年cv.LG
* domain: computer vision

### Abstract
* 在训练由于前面层的参数的变化，会导致本层输入分布的变化，因此导致训练一个DNN十分复杂，我们不得不降低训练速度和小心的初始化.这种现象被成为internal covariate shift.
* 解决上述问题，通常采用的方法是normalize输入层.我们的方法力图使规范化成为模型架构的一部分，并为每个训练小批量执行归一化.
* Batch Normalization允许我们使用更高的学习率和更少的关注初始化，并且它也可以作为一个regularizer，同时不需要dropout的使用.

### Introduction
* 输入的分布属性可以使训练更加高效，原因是如果本层输入数据分布保持固定，即使上一层输入数据分布发生了改变，也不需要重新进行进行本层参数用于补偿上一层的变化.
* 饱和问题和梯度消失近几年通常使用ReLU、careful initialization和small learning rate来解决.

### Towards Reducing Internal Covariate Shift
* **Internal Covariate Shift defines as:**  
由于网络参数在训练期间的改变导致网络激活分布的改变.

### Normalization via Mini-Batch Statistics
* 由于每层输入全进行白化代价过高，这里提出两点简化: (1)代替白化，我们独立使每个scalar feature做均值为0且方差为1的归一化(2)由于我们使用的是mini-batches sgd进行训练，因此我们使用每个mini-batch进行每个activation的均值和方差的评估.
* 数据归一化方法很简单，就是要让数据具有0均值和单位方差，如果简单的这么干，会降低层的表达能力.比如在使用sigmoid激活函数的时候，如果把数据限制到0均值单位方差，那么相当于只使用了激活函数中近似线性的部分，这显然会降低模型表达能力.为此，作者添加了两个参数，用来保持模型的表达能力.其实是一个仿射变换(scale and shift). ![1](https://cloud.githubusercontent.com/assets/16068384/25042342/e79902e2-2149-11e7-9e49-072413618007.png)
 其实，当两个参数取特定值时，可以恢复到原始的某一层学到的特征.
* BN的forwardpropogation和backpropogation  
![1](https://cloud.githubusercontent.com/assets/16068384/25042084/c5314d7e-2147-11e7-8fff-1d710f7df71d.png)
![2](https://cloud.githubusercontent.com/assets/16068384/25042087/c8478af0-2147-11e7-99d6-c08ed065c631.png)
* 训练过程中,用一个Batch的均值和方差作为对整个数据集均值和方差的估计,用一个Batch的均值和方差作为对整个数据集均值和方差的估计. 但是在测试过程中，使用的是整体的均值和方差.![1](https://cloud.githubusercontent.com/assets/16068384/25042418/7459c996-214a-11e7-8c76-213a3eaf4c23.png)

### BN的优势
* 增大学习率
* 可以移除dropout
* 降低L2权重衰减系数
* 加速学习率衰减
* 可以移除LRN
* 在我们方法中对训练数据进行更彻底的洗牌
* 减少图像扭曲的使用

### ensemble 6个模型，达到了state-of-the-art的水平


### 我的扩展
* 对输入数据进行预处理，减均值->zscore->白化可以逐级提升随机初始化的权重对数据分割的有效性(学习速度)，还可以降低overfit的可能性

### 源代码
* 作者在文章中说应该把BN放在激活函数之前，这是因为Wx+b具有更加一致和非稀疏的分布。但是也有人做实验表明放在激活函数后面效果更好。这是实验链接，里面有很多有意思的对比实验：https://github.com/ducha-aiki/caffenet-benchmark
* 在caffe的官方版本中把bn算法分成了两个层，一个是batch_norm_layer,另一个是scale_layer.使用实例可参考https://github.com/KaimingHe/deep-residual-networks/blob/master/prototxt/ResNet-50-deploy.prototxt. 同时，在我的项目CaffeAnalysis中对两个layer进行了分析.
* caffe的bn分支对于bn的实现: https://github.com/ducha-aiki/caffe/blob/bn/src/caffe/layers/bn_layer.cpp
