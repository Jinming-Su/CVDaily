# 引介
Yu F, Koltun V. Multi-scale context aggregation by dilated convolutions[J]. arXiv preprint arXiv:1511.07122, 2015.  
所属领域为图像语义分割  

# Abstract
在本文的工作中，开发了一种新的卷积网络模块，专门设计用于dense prediction.本文提出的模型痛殴使用dilated convolutions系统化集成了multi-scale上下文信息，并且没有损失分辨率.这个架构是基于dilated conv在不损失分辨率和范围情况下能够指数级增长分辨率.

# Introduction
FCN提出的CNN架构最初是设计用于分类的，在分割上取得了成功.但是分类和分割结构化的不同导致了新的问题.重用网络的哪些方面是真正必要的，哪些在密集操作时降低精度？专门用于密集预测的专用模块可进一步提高精度吗？  
dense predicton需要multi-scale的上下文信息，并且也需要full-resolution outpu.一种解决方法是重复使用up-conv，目的是在从低采样层传承全局视野的同时复原损失的分辨率.这遗留了一个问题是是否严格的中间采样层真的需要.另一个问题是提供图片的不同尺寸作为输入，结合这些预测.这导致的问题是不清楚是否需要对重新调整的输入图像进行单独分析.  
于是，本文提出了一种conv module，集成不同尺度的上下文信息，而不损失精度，也不需要分析多个尺度的图片.  

# Dilated Conv
【遗留问题】公式看的不是特别懂

# Multi-scale Context aggregation
context module设计用来通过集成multi-scale contextual information来增加dense prediction架构的性能.basic context module有7层3x3的卷积，dilations分别是1,1,2,4,8,16,1.这些卷积后都是用ReLU函数.  
![1](http://i4.buimg.com/589172/61102078a01ea8b9.png)  
实验辨明，通过标准的初始化步骤不能轻易地进行module的训练，因此采用了一种特殊的初始化方法.【需要细看】  

# Conclusion
本文工作表明了，dilated conv操作由于起能够不损失分辨率和覆盖的能力非常适合进行dense prediction.  

# 相关资料
* 本文还专门介绍了3中urban scene 数据集.
* 源代码： https://github.com/fyu/dilation
