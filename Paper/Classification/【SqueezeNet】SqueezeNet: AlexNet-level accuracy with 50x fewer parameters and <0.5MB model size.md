# 基本情况
2016年写的投ICLR 2017的文章.主要针对模型压缩的.使用的是分类网络中的AlenNet为代表.  

# Abstract 
目前很多方法都是只关注精度的，但是在同等精度的情况下，小的模型很多优点，比如：（１）训练等更快（２）在部署时更少的带宽要求，例如自动驾驶汽车（３）可以部署到FPGA等.正是由于有这些优点，本文提出了一种小的CNN架构，SqueezeNet.实现了AlexNet模型参数减少了50倍.在受用模型压缩技术情况下，可以做到减少510倍参数，只有0.5MB的模型大小.  

# Related work
模型压缩方面：本文工作的首要目标是确认一个模型，保证精度的情况下使用很少的参数.目前已经有许多模型压缩的方法了：SVD；设置阈值的方法；Deep Compression等.  
CNN网络模块方面：目前有Inception modules等.  
CNN网络架构方面：目前有bypass connections等.  

# SqueezeNet: 保持精度减少参数
本文针对保持精度减少参数提出了三个策略：（１）使用1x1filters来代替3x3filters（２）减少3x3filters的输入通道数（３）推迟下采样，保证网络有大的activation maps.很容易看出来，（１）（２）是为了减少参数的，而（３）是为了在限制的参数数量条件下提高精度的.  
针对（１）（２）本文提出了一种网络模块Fire Module.  
![1](http://i4.buimg.com/589172/fac7c76a819a8655.png)  
针对（３），本文对Fire Module进行了组合，创建了SqueezeNet.
![1](http://i4.buimg.com/589172/6c09ea29086df67e.png)  

# Evaluation of SqueezeNet
这部分做了本文提出的性能与其他方法的比较.  
![1](http://i4.buimg.com/589172/c85608313ba921a4.png)  

# CNN exploration
这一部分来分析Fire Module中超参数的合适取值，来保证准确率.  
![1](http://i4.buimg.com/589172/ea53c71379f173b2.png)  
接着实验说明了bypass结构的使用对结果的影响.  
![1](http://i1.piimg.com/589172/d869beeaf2a650b0.png)  

# 相关资源
* 项目主页: https://github.com/DeepScale/SqueezeNet
