---
title: 【crfasrnn】Conditional Random Fields as Recurrent Neural Networks笔记
date: 2017-04-17 00:00:01
categories:
- Deep_Learning
- Paper
tags:
- crfasrnn
description: crfasrnn
---
### 基本信息
* time: ICCV2015
* domain: semantic segmentation

### Abstact
* 近些年有方法都尝试利用dnn的能力实现semantic segmentation任务.但是，这种方法的一个核心问题是深度学习技术描绘视觉对象的能力有限.
* 为了解决上述问题，本文提出了一种新的形式的CNN，它结合了CNNs和CRFs.我们的方法把CRF集成到CNNs中，实现了整个网络的end-to-end的训练，避免了为了物体勾画的offline post-processing.

### Introduction
* 为了实现好的语义分割，feature representation十分重要，同时，image edges、appearance consistency和spatial consistencyt也很重要.
* **使用CNN的动机**  
the key insight是学习像素级标签任务的端到端的强功能表征，而不是使用启发式参数调整手工制作功能.
* **传统的用于Object Recognition的CNN很难转换为用于segmentation的 pixel-wise predicting**  
(1)感受野过大以及pooling操作使的feature map很coarse,例如可能导致non-sharp的边界和blob-like shapes(2)缺少smooth机制（相似像素标签一直、空间和表面一致性等）导致poor object delineation和small spurious region(假区).我们希望两个相邻的像素如果差别越大，那么这两个像素属于不同类别的概率应该越大；如果两个相邻像素点的颜色非常接近，那么它们属于不同类别的概率应该越小.因此如果能够把这些人工已有的先验约束信息加入其中，那算法就会有进一步的提升.
* **CRFs**  
当前，概率图模型常常被用于提高pixel-wise labeling tasks的精确度.主要是MRFs和CRFs.CRF预测的主要思想是: 把pixel的label标记问题转化为概率预测问题,其中包含了类似像素之间的标签一致等假设.CRF预测能够提取weak和coarse的预测来产生sharp boundary和fine-grained(精密细纹)的分割.
* **CRF-RNN**   
本文的原理是利用平均场近似CRFs的过程转化为RNN，并把CRF-RNN嵌入到CNNs中，进行forwardpropogation和backpropogation来训练模型.

### Related Work
* **现在用CNN解决语义分割的方法主要两类**  
(1)利用图片的egdes，使用分离机制进行处理，通常基于proposal(如superpixels).主要缺点是前期的proposals很重要(2)直接基于pixel进行处理.
* NN已经被用于很多领域
* 图模型的自动参数学习方法也有很多.

### A Mean-field Iteration as a Stack of CNN Layers
* 公式
![1](https://raw.githubusercontent.com/su526664687/PictureLibrary/master/Paper/Crfasrnn.png)
* 不像CNN的卷基层filters参数在训练之后是固定的，我们使用边缘保留高斯滤波器，其系数(filters)取决于图像的原始空间和外观信息.
* **Initialization**
相当于在每个像素的所有标签上对一元势能U使用soft-max function. backpropogation过程就是softmax的bp.
* **Message Passing**  
类似卷基层
* **Weighting Filter Outputs**  
看成1 x 1 x M卷积核的卷积，有一个输出
* **Compatibililty Transform**  
看成1 x 1 x L卷积核的卷积，有L个输出
* **Adding Unary Potentials**  
没有参数，bp直接拷贝就可以了
* **Normalization**
相当于一个softmax过程

### The End-to-end Trainable Network
* CRF-RNN只训练两种参数: 高斯核的权重和兼容性参数.为了简单，高斯核的带宽（标准差，即theta参数）是固定的，也就是高斯核函数是固定的.
* 使用mean-field算法计算Dense CRFs少于10次就可以收敛，大约在5次之后结果的提升已经不明显了.因此，可以不会出现梯度弥散和梯度爆发的现象，也就是可以使用朴素的RNN结构，而不需要使用更复杂的诸如LSTMs等结构.

### Effect of Design Choices
* 作者在实验过程中发现了一些提高性能的小方法  
(1)设置不同的filter weight和引入非对称个的兼容性函数(2)设置T=5train during training和t=10 during testing.可能的原因是梯度弥散，表现为一元势能在training期间收到一个weak error gradient signal导致妨碍学习性能.(3)end-to-end提高了系统的准确性(4)RNN很重要.

### 源代码
* caffe model zoo
* 代码解读： http://blog.csdn.net/taigw/article/details/51794283
