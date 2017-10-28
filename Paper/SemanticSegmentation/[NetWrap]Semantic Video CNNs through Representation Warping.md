ICCV2017的文章，arXiv:1708.03088 [cs.CV]，德国的几个研究院所与NVIDA合作的文章.  

# Abstract
提出了一种方法将用于静态图片语义分割的CNN架构转化为能够用于视频图像进行语义分割的CNN架构.  
主要采用的思想使用增强现有的架构，具体使用方法是添加NetWrap模块，借助的主要信息是optical flow的计算和整合.  
最终达到在CamVid和Cityscapes上的sota(state-of-the-art).  

# Related Works
对于视频数据的语义分割，一种朴素的做法是直接进行单帧的分割，这种方法存在严重的抖动，尤其是物体的边界位置，修正的方法是添加CRF，但是这并不是一种优雅的做法，并且实际应用中通常会很慢.  
还有的方法就是通过3D-2D信息联合，从3D中获取到运动的信息，协助2D进行视频语义分割，但是3D数据很难获取.  
还有的做法是使用双向的filter进行跨多个帧的长范围的信息传播.  
还有的做法是重用之前帧的CNN的中间表示.  

# Models
### 动机
原文参考文献[39]的作者表明，CNN的中间表示在相邻帧之间仅缓慢变化，特别是对于较深的CNN层，这启发了钟表控制架构的设计；在[13]中，作者构建了一个双边模块，用于平均跨越图像空间和光度接近的位置的中间CNN表示.  
本文的做法就是在CNN的中间表示层，在相邻两帧之间结合时间和广度表示，使得结果更加稳定和一致.  
![这里写图片描述](http://img.blog.csdn.net/20171028131353076?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDQ1MTA3Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  

### NetWrap
![这里写图片描述](http://img.blog.csdn.net/20171028131438853?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDQ1MTA3Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
**光流的计算:**  采用已经的方法在现在帧和上一帧之间进行计算光流，计算出的应该是一个光流矢量，用于两帧之间的映射.本文计算的是reverse flow.  
**光流的转化:**  直接使用传统方法计算出的光流可不能不是最优的，于是又放在一个CNN中进行转化.  
**变形表示:**  z'(t-1) = Warp(z(t-1), 光流转化)， z(t-1)表示上一帧的featuremap，z'(t-1) 表示warped representation.  
**表示的组合:** 将z(t)和z'(t-1)进行线性组合，得到z'(t)  
**训练:** 四个输入:data0, data1, flow1, conv，分别表示现在帧，上一帧，上一帧的optical flow，以及上一帧在指定层添加NetWarp的featuremap，然后在CNN过程中添加将z'(t)添加到网络中进行训练.（代码在PSPNet上的做法）  

### 实验
在CamVid上，采用Dilated、PlayData，在Cityscapes上使用PSPNet分别进行了添加NetWarp的尝试，均达到了新的sota，比原有方法性能提高一到两个百分点.

# Summary
个人看法，本文最大的贡献就是考虑到引入一种结构，将用于图片的CNN能用于视频。算是一个trick吧，在以后视频图像中也会考虑到optical flow应该作为一种信息使用。

# Thinking
* 本文的实验作者实际隐含认为视频帧之间满足马尔科夫性

# References
* [13] R. Gadde, V. Jampani, M. Kiefel, D. Kappler, and P. Gehler. Superpixel convolutional networks using bilateral inceptions. In European Conference on Computer Vision. Springer, 2016
* [39] E. Shelhamer, K. Rakelly, J. Hoffman, and T. Darrell. Clockwork convnets for video semantic segmentation. arXiv preprint arXiv:1608.03609, 2016.
* 代码: https://github.com/raghudeep/netwarp_public
