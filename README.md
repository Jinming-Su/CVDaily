---
title: 我的深度学习入门过程
date: 2017-03-02 00:02:01
categories:
- Deep_learning
tags:
- deep_learning
description: ...
---

    
> 这里开始，我准备写一个深度学习(deep learning, 下文简称dl)的简单的入门教程.  
  其实就是我的dl入门的过程，学习了一段时间之后，回过头来进行整理.

### 起源
* 之所以搞深度学习是因为读研的方向是计算机视觉(CV)，需要使用dl作为工具进行实现.
* 同时，大四毕业设计的题目也是通过使用dl实现语义分割.

### 过程
* 首先是计算机视觉（computer vision， 下文简称cv）的入门，这个参考[知乎上@方杰](https://www.zhihu.com/question/26836846/answer/34322576). 我仔细浏览了一遍stanford cs131的课程，对cv有了一个整体的认识,可以看[我的总结](https://github.com/su526664687/Articles/blob/master/deep_learning/Computer%20Vision:%20Foundations%20and%20Applications_summary.md).这个课程讲解的都是一些经典的cv处理方法，并没有涉及dl.
* 很快，师兄推荐了论文fully convolutional network for semantic segmentation.fully xxx这篇paper是dl应用与图像分割的开山之作.第一次读这样的文章难免会很多不懂的地方，可以结合这一篇imagenet classification with deep cnn, 这篇是dl的开山之作.
* 读论文的同时，我也在学习stanford的cs231n课程(资源可以在xx云课堂上找到)，这个课程令我对神经网络和CNN的大部分概念有了深入的理解，并了解了RNN等，这是[我的笔记](https://github.com/su526664687/Articles/blob/master/deep_learning/%20Convolutional%20Neural%20Networks%20for%20Visual%20Recognition_summary.md).其实之前师兄推荐的论文并没有读的很懂,在学习cs231n的过程中，了解到了几个经典的machine learning的算法，通过matlab进行了实现:
    * [knn](https://github.com/su526664687/Articles/blob/master/deep_learning/matlab%E5%AE%9E%E7%8E%B0:%20knn.md)
    * [svm](https://github.com/su526664687/Articles/blob/master/deep_learning/matlab%E5%AE%9E%E7%8E%B0:%20svm.md)
    * [线性回归和logistic(待续)](https://github.com/su526664687/Articles/blob/master/deep_learning/*matlab%E5%AE%9E%E7%8E%B0:%20%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92%E4%B8%8Elogistic.md)
* 下一步就开始正经的进入到dl的学习与实践当中了.
    * git caffe,如果不会git，可以去学习[廖雪峰git]()
    * 安装caffe并尝试训练了例程mnist和cifar10.[安装教程](https://github.com/su526664687/Articles/blob/master/deep_learning/caffe/ubuntu%E6%97%A0cuda%E5%AE%89%E8%A3%85caffe.md).刚开始测试mnist，虽然能跑通结果，可是完全不懂是做什么，这里我谢了一个代码，可以把[mnist中idx3-ubyte转化为图片](https://github.com/su526664687/Articles/blob/master/deep_learning/caffe/matlab%E5%AE%9E%E4%BE%8B:%20mnist%E4%B8%ADidx3-ubyte%E8%BD%AC%E5%8C%96%E4%B8%BA%E5%9B%BE%E7%89%87.md).这样就可以直观看到，mnist例程是测试一些手写图片.
    * 根据官方文档[安装和使用matcaffe](https://github.com/su526664687/Articles/blob/master/deep_learning/caffe/matcaffe%E5%85%A5%E9%97%A8.md)
    * [自己训练和测试数据](https://github.com/su526664687/Articles/blob/master/deep_learning/caffe/%E3%80%90%E5%85%A5%E9%97%A8%E5%AE%9E%E4%BE%8B%E3%80%91%E7%94%A8LeNet%E8%B7%91%E8%BD%A6%E7%89%8C%E8%AF%86%E5%88%AB%E6%95%B0%E6%8D%AE.md)
    * [跟着博客学习，深入理解](http://blog.csdn.net/gybheroin/article/category/6665870)
    * 完成到这一步，基本已经十分了解alexnet，以及lenet, caffenet等.  
    <font color="red"><b>指的是</b></font>: 可以自己从0开始在caffe上实现一个alexnet，进行训练并测试，了解每一层和每一个数据块的含义.并使用matlab进行过对alexnet等的单步调试.
* 下一步，开始玩fcn,进行图像语义分割(待续)
    * 先对[fcn进行测试和训练](https://github.com/su526664687/Articles/blob/master/deep_learning/caffe/*FCN%E6%B5%8B%E8%AF%95%E4%B8%8E%E8%AE%AD%E7%BB%83.md)

### 我的资源
* [本科毕业设计进度](https://gist.github.com/su526664687/7e3c40909e2a80243441bb0acb0928a4)

### 参考
* [师兄推荐的下载论文的地方](http://www.ipcv.org/category/conf-jour/cvpr/)
