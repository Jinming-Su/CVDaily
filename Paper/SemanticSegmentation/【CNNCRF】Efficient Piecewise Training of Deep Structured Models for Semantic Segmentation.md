# 基本情况
本文是CVPR 2016的文章，领域是Semantic Segmentation.  

# Abstract
本文展示使用上下文信息提高语义分割.特别的，本文使用图片区域的'patch-patch'的上下文和'patch-background'的上下文.在从patch-patch的学习过程中，本文使用基于CNN的成对势能函数的CRFs来捕获相邻块中的语义相关性.利用本文提出的深度结构模型的高效piecewise训练来避免后向传播过程中CRF预测的消耗.为了捕获patch-background上下文，本文使用了传统的多尺度图片输入和滑动金字塔池化的网络设计来高效地提高性能.本文的结果在很多数据集上达到了新的state-of-the-art，包括NYUDv2,PASCAL VOC 2012, PASCAL-Context和SIFT-flow.

# Introduction
由于FCNNs对于语义分割高效计算能力和end-to-end的学习方式，已经成为语义分割领域最受欢迎的选择.  
**两种上下文**  
在场景理解任务中，上下文关系是无处不在的并且为分割提供了重要的线索.空间上下文关系可以提供物体的兼容关系，例如汽车可能展示在公路上，当然，也编码包含不兼容关系，例如汽车不可能在天空中.当然也存在part-to-part和part-to-object的关系.  
本文提出了两种类型的空间上下文来提高分割性能：patch-patch上下文和patch-background上下文.  
关于如何精确的建模patch-patch上下文关系，在最近中CNN-based分割方法中还没有很好的研究.本文提出了一种使用CRFs的方法.使用CNN-based的成对势能函数来捕获相邻patches中间的语义关系.和其他使用CRFs来勾勒区域边界不同，本文的CNN成对势能主要是为了提高coarse-level的预测.  
patch-backround在最近的文献中被广泛利用.CNN-based的方法可以通过利用malti-scale图片输入来捕获背景信息.本文使用multi-scale网络和sliding pyramid pooling来编码丰富的背景信息.  
由于成对势能在预测阶段耗时较多，本文为了高效学习，使用pecewise的方法训练CRF(不太明白).  
本文主要贡献如下:  
(1) 本文方程化了CRFs中的CNN-based通用成对势能函数，来精确建模patch-patch语义关系.  
(2) 由于深度的CNN-based通用成对势能对于高效的CNN-CRF联合学习很困难，因此使用近似的训练方法－piecewise训练.  
(3) 通过使用传统的multi-scale输入和sliding pyramid pooling来研究背景上下文.  
(4) 在多个数据集上达到了state-of-the-art.  
# Modeling semantic pariwise relations
![1](http://i1.piimg.com/589172/2a6c81feb51551a6.png)  
![1](http://i1.piimg.com/589172/b2493cbc3ca50957.png)  
不理解途中generate features做了什么.  

# Contextual Deep CRFs
这部分讲解了本文提出的Deep CRFs结构，这里一元势能和二元势能的获取如图3中所示.  

# Exploiting background context
![1](http://i1.piimg.com/589172/c07ac5c52b00ddd4.png)  
也就是利用多尺度和滑动金字塔结构来编码背景信息.  

# Prediction
参考图3，经过FeatMap-Net先生成原图1/16的特征图.然后进行两个阶段的转化，得到最终结果.  
第一个阶段是Coarse-level prediction stage，也就是deep CRFs阶段，第二个阶段是先upsampling到原图，然后dense CRFs.  

# Reference
* [3] deeplabv1
* [13] Learning hierarchical features for scene labeling.
* [32] FCN
* [33] zoom-out
* [35] deconvnet
* [40] A. G. Schwing and R. Urtasun. Fully connected deep
structured networks, 2015.
* [48] crfasrnn
