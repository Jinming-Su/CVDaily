---
title: 【SegNet】SegNet:A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation笔记
date: 2017-04-15 00:00:01
categories:
- Deep_Learning
- Paper
tags:
- SegNet
description: Segnet
---
### 基本情况
* time: 2015CVPR
* domain: semantic segmentation

### Abstract
* 提出了SegNet，核心的训练引擎包含一个encode网络，接上一个decoder网络，并跟随一个pixel-wise分类层.
* 通过比较SegNet和FCN的相关方法，揭露在segmentation时内存和准确度的对应.
* 利用SegNet做了在Camvid和SUN RGB-D indoor的评测.

### Introduction
* **目前方法存在的问题**  
近期的许多semantic segmentation研究采用dnn，但是结果比较粗糙，主要原因是max-pooling和sub-sampling降低了feature map的分辨率.(我认为sub-sampling是一类方法，而max-pooling是前者的一种实现)
* **设计SegNet的动机**  
road scene understading需要算法具有mode外形、shape和理解空间关系(上下文)的能力.由于是公路场景，因此需要网络能够产生光滑的分割，网络也必须有能力勾画出小尺寸的物体.因此在提取图片特征过程中保留边界信息很重要.
* **重用max-pooling indices的优点**  
(1)提高边界勾画(2)减少了进行端到端训练的参数(3)这种upsampling的形式可以被集成到任何encoder-decoder架构的网络中.
* 对于PascalVOC，作者指出该数据集中有少数foreground与background有明显区分，这让一些投机者可以使用类似于边缘检测来刷分数.因此作者使用了Camvid，Sun这两个数据集，而不是用PascalVOC数据集.

### Literature review
* **dnn之前**  
手工提取特征得出的结果以后，由于边界模糊，一般大家都使用CRF进行结果的平滑
* **FCN**  
FCN的encoder network有134M，而decoder network只有0.5M。如此多的参数让网络很难训练.因此fcn作者使用了stage-wise training process.FCN除了training的时候很麻烦，在inference的时候也因为参数过多显得很麻烦.
* **CRF-RNN**   
FCN提出了以后，有人提出了CRF-RNN这种post-processing的方法。使用FCN-8网络加上CRF-RNN这种后处理方法得到的结果比FCN-8的结果要好.也可以在segnet后面也可以加上CRF-RNN.
* 目前提出的一些网络不是feed-forward（前馈型）网络，他们要么需要在CRF上求MAP来进行inference，要么需要借助region proposal来进行inference.作者认为之所以这些方法盛行是因为没有找到在前馈型网络中没有找到合适的decoder方法。而segnet找到了
* **DeconvNet**  
DeconvNet中的来自VGG16的全连接层参数占据了总网络的90%，这导致训练困难，需要使用region proposals.

### Architecture
* **抛弃fc层**  
抛弃fc层为了保证在encoder的最深输出处保持高分辨率，并且减少了encoder的参数数量(从124M到14.7M)
* 使用了batch normaized, ReLU
* max-pooling被用于去实现在input image的小的空间变换中的平移不变性；Sub-sampling results in a large input image context (spatial window) for each pixel in the feature map.
* **SegNet和FCN的decoders的不同**  
SegNet是使用unpooling+convolution实现；而FCN是使用deconvlution实现.
* 使用cross-entropy loss；因为天空，建筑，自行车的像素点在训练集中占据的比例有很大的差距，因此需要在计算loss的时候采用median frequency balancing.
* summary  
![1](https://cloud.githubusercontent.com/assets/16068384/25061402/0d3a04ee-21e8-11e7-88b3-8fffd899658c.png)

### Benchmarking
* 使用CamVid数据集作为Segnet的benchmark, 并结合多个数据集做了一个ensemble作为segnet的额外的benchmark
* 在CamVid上的结果:DeepLab-LargeFOV是其他的model里面最有效率的model，DeepLab-LargeFOV加上denseCRF的后处理的结果可以与segnet匹敌;Deconvnet网络参数最多，最难训练，并且没有划分出小物体;FCN with learnt deconvolution is clearly better than with fixed bilinear upsampling;同时比较比较了SegNet和非dl的方法.
* 在SUN RGB-D Indoor Scenes上，需要分割37类室内物体，类别更多.

### Discussion and future work
* 在对不同参数化的不同深层架构进行基准测试时，我们必须做出的一个重要选择是训练他们的方式.他们各自的多阶段训练或者独特的技术导致比较他们的时间和精度比较困难.这里同事使用batch normalization和sgd来保证end-to-edn的训练.

### 其他分析
* caffe-segnet: https://github.com/alexgkendall/caffe-segnet  
prototxt文件: https://github.com/alexgkendall/SegNet-Tutorial
* 有两种SegNet的实现，一种是正常版，另一种是贝叶斯版
* 模型中使用的same convolution
* 参考: http://blog.csdn.net/fate_fjh/article/details/53467948
