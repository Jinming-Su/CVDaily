# 引介
arXiv:1612.01105 [cs.CV]，所属领域为Semantic Segmentation.

# Abstract
场景解析对于无限制的开放词汇和不同场景来说是具有挑战性的.本文使用文中的pyramid pooling module实现基于不同区域的上下文集成，提出了PSPNet，实现利用上下文信息的能力进行场景解析.

# Introduction 
很多State-of-the-art的场景解析框架都是基于FCN的.基于CNN的方法能够增强动态物体的理解，但是在无限制词汇和不同场景中仍然面临挑战.举个例子，如下图.  
![1](http://i2.muimg.com/589172/6a7a886c0beef083.png)  
FCN认为右侧框中是汽车，但是实际上是船，如果参考上下文的先验知识，就会发现左边是一个船屋，进而推断是框中是船.FCN存在的主要问题就是不能利用好全局的场景线索.  
对于尤其复杂的场景理解，之前都是采用空间金字塔池化来做的，和之前方法不同（为什么不同，需要参考一下经典的金字塔算法），本文提出了pyramid scene parsing network(PSPNet).  
最终，本文的方法取得了ImageNet scene parsing2016的第一名，PASCAL VOC 2012 semantic segmentation的第一名，以及Cityscapes的第一名.  
本文的主要贡献如下:  
(1)提出了PSPNet在基于FCN的框架中集成困难的上下文特征  
(2)通过基于深度监督误差开发了针对ResNet的高效优化策略  
(3)构建了一个用于state-of-the-art的场景解析和语义分割的实践系统（具体是什么？）  

# Related Work
再一次阐述了，基于FCN的方法，只要有两个研究方向：一个是multi-scale的特征整合，另一个是结构预测（CRF等）.  

# PSPNet
通过观察FCN的结果，发现了如下问题：  
(1)关系不匹配（Mismatched Relationship） 
(2)易混淆的类别（Confusion Categories）
(3)不显眼的类别（Inconspicuous Classes）  
总结以上结果发现，以上问题部分或者全部与上下文关系和全局信息有关系，因此本文提出了PSPNet.框架如下:  
![1](http://i2.muimg.com/589172/e4fd6b598cbca1a2.png)  

# Experiments
本文除了使用Pyramid pooling module外，还用了多个tricks：DR(dimension reduction), AL(additionial loss), DA(data augmentation), MS(multi-scale testing).  

# Reference
* [3] deeplabv1
* [4] deeplabv2
* [13] ResNet
* [17] AlexNet
* [24] ParseNet
* [33] VGGNet
* [34] GoogLeNet
* [26] FCN
* [30] DeconvNet
* [40] F. Yu and V. Koltun. Multi-scale context aggregation by di-
lated convolutions. arXiv:1511.07122, 2015.
* [41] CRFASRNN

# 相关资料
* 项目主页: https://hszhao.github.io/projects/pspnet/
* 源代码(没有模型文件): https://github.com/hszhao/PSPNet
* 复现效果似乎不好，参见知乎上的评论：https://www.zhihu.com/question/53356671/answer/144164564
