# 引介
文章提出的网络在PASCAL VOC2012和Cityscapes上都叫TuSimple，不过文章读起来确实挺简单的.  
这篇文章是2017年2月的文章，所属领域为Semantic Segmentation.  

# Abstract
本文展示了如何通过操纵更适合实际使用的卷积相关操作来改进像素级语义分割.首先，本文实现了dense upsampling convolution(DUC)来产生像素级别的预测，目的是捕获和编码更加细节的信息.然后，提出了一种hybird dilated convolution(HDC)框架用于编码阶段的使用，目的是改善由于dilated convolution造成的'gridding issue'.  
本文提出的方法在Cityscapes和KITTI以及PASCAL VOC 2012当时都达到了state-of-the-art.  

# Introduction
在Semantic segmentation领域，目前最好的方法通常有一下三个组成部件：（１）FCN（２）CRFs（３）dilated convolution.自从FCN引入SS之后，研究人员主要关注两个方面来提升性能：（１）更深的FCN models（２）能强大的CRFs.而本文另辟蹊径，考虑从另一个角度提升SS性能：编码和解码过程中的卷积运算.解码提出了DUC，编码提出了HDC.  
# Our Approach
**DUC**  
针对无法学习的二次上采样和反卷积需要先填充0进行反池化和卷积操作的确定，本文提出DUC使用卷积操作直接生成pixel-wise的预测图.DUC结构图示如下：  
![1](http://i1.piimg.com/589172/67d28f19ef20129f.png)  
原文描述得简单易懂:  
![1](http://i1.piimg.com/589172/d1fb872540240a1c.png)  
DUC对相对小的物体识别得很好.  

**HDC**  
这部分主要是针对dilated conv的"gridding issue".这种现象图示如下：  
![1](http://i1.piimg.com/589172/6e90d4e277a3e7af.png)  
简单描述就是如果多个层的dilation是一样的，那么网络贡献的数值只有那些稀疏的点上的数值，当dilation变大的时候，由于downsampling等操作来自input的采样会更加稀疏，局部信息可能完全丧失，同时大距离的信息也可能不再相关.  
本文为了改进这个问题，把dilatioin rate变成锯齿形式的，也就是不同层之间的dilation不断变化，导致了Fig2(b)的结果.  
HDC的另一个优点是，由于dilation rates可以是任意的，所以能够天然增大网络的感受野，对于识别相对大的物体表现得很好.  
有个需要注意的地方，本文认为，在一组中的dilation rate不应该有公因子关系，否则gridding issue会仍然存在.  

# Experiments
接着就是实验部分，具体细节参看原文，效果确实不错.  
![1](http://i2.muimg.com/589172/21b91380f2e72fd4.png)  

# 相关资料
* 源代码，MXNET实现: https://goo.gl/DQMeun
