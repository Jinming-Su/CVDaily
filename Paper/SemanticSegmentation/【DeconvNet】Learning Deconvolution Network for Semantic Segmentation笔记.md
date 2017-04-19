---
title: 【DeconvNet】Learning Deconvolution Network for Semantic Segmentation笔记
date: 2017-04-13 00:00:01
categories:
- Deep_Learning
- Paper
tags:
- deconvolution
description: DeconvNet
---
### 基本情况
* time: 2015年ICCV的一篇文章
* domain: semantic segmentation

### Abstract
* 提出深度反卷积网络: 实在vgg16的顶部添加反卷积层.反卷积层由deconvolution、relu和upooling组成.
* 通过把每一张图片的不同的proposal送入deploy的网络，通过aggregate得到最后的语义分割结果.
* 改进之处: 针对基于FCN的方法（FCN感受野固定），实现处理精细的结构以及不同尺度大小的目标.

### Introduction
* 基于FCN的方法最大优势是:输入整张图片、快速运行、准确推理.
* 基于FCN的方法的缺点是:(1)感受野固定，导致过大的物体可能不会被分块或不连续，过小的物体容易被忽视.FCN虽然使用了skip architecture，但是根本的解决方案是详细的边界和语义.(2)输入反卷积层的label map太粗糙，反卷积过程太简单，使得物体的细节信息丢失或被平滑.
* 为了解决上述两个问题，本文有一下主要贡献:(1)提出了一个deep deconvolution network.(2)对于每张图片使用多个proposal进行预测，最后进行aggregate，得到最后的预测结果.(3)将FCN的结果和本文的结果结合起来，获得目前最好的语义分割结果.

### System Architecture
* 在VGG16的基础上，移除softmax层，添加对称的deconvolution、unpooling、relu
* **Pooling层**  
的作用是通过在一个感受野提取代表性的激活值，来过滤激活噪声；优点是在上层保留鲁棒的激活值，有利于分类；缺点是pooling 过程中一个感知野的空间信息丢失，不利于semantic segmentation等要求精确定位的任务；本文给出的解决方法是首先在pooling的时候用switch variables记录max pooling 选择的最大值的location，然后在Unpooling层利用switch variables还原回原location，从而恢复成pooling前同样大小，其它像素应该是用0代替，得到稀疏的响应图.
* **Deconvolution层**   
在unpooling之后得到稀疏响应图，然后可以通过deconvolution使稀疏响应图变得稠密.
* 在反卷积结构中，lower layers扑捉物体总体的形状；higher layers编码了特定类别的细节信息；
* 本文实质是将semantic segmentation问题视为instance  segmentation问题. 原因是: instance segmentation可以处理不同尺度大小的目标； ***并且可以减少搜索空间，减少训练的复杂度减少存储需求(不明白)***

### Training
* **BN**  
利用Batch Normalization避免陷入局部最优
* **Two-stage**  
第一阶段，利用ground-truth 裁剪object instances ,使目标位于裁剪的bounding box的中心，进行训练；第二阶段，利用object proposals构造更加具有挑战的样例，进行 fine-tune.  

### Inference
* **Aggregate**  
每张图片的object proposals进行aggregate,这里采用取最大值的方法.
* **Ensemble**  
将本文的结果与FCN的结果ensemble，这里采用mean的方法.并把结果输送fcCRFs.

### 源代码
* 项目主页: http://cvlab.postech.ac.kr/research/deconvnet/
* https://github.com/HyeonwooNoh/DeconvNet
* 这里我在看的时候存在一个问题，就是generate_EDeconvNet_CRF_results.m中line 115位置，FCN与DEconvNet进行ensemble的时候使用的是'.*'，而不是论文中说的mean方法.
