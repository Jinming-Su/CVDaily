# 基本情况
2017年4月份的文章，所属领域是Semantic Segmentation.

# Abstract
本文主要是针对realtime semantic segmentation问题.本文提出的方法减少了大量的计算，这个方法是基于PSPNet压缩的图片级联网络(ICNet)，在合理的标签指导下结合多个分支来实现较少计算的目的.接着，本文又深度分析了本框架，并引入cascade feature fusion实现高质量的快速分割.最后，在Cityscapes上实现相当不错的结果.  

# Instroduction
现在，大多数的方法都是通过增加参数（网络的深度宽度）来实现更高的分辨率，尤其是FCNs-based方法.  
![1](http://i1.piimg.com/589172/d9f788b818e85511.png)  
从图中分析，实时语义分割会有许多应用：例如自动驾驶、机器人交互、在线视频处理、甚至手机计算等.  
在本文中，作者主要意图是建立一个具有相当的精确度的具有实用价值的快速图像分割系统.主要方法是，利用低分辨率图片的高效处理和高分辨率图片的高推理质量，来提出了一个图片级联框架实现分割.  
本文的主要贡献为:  
(1)提出了一个图片级联网络(ICNet)，它利用低分辨率的语义信息和高分辨率的细节信息.  
(2)提出的ICNet完成了5x+的推理提速，并减少5+的内存消耗.  
(3)实现1024x2048分辨率图片30.3fps分割性能.  
# Related work
实时的物体检测已经发展的不错了，可是实时的SS才刚刚开始，SegNet通过抛弃fclayer来减少网络参数，ENet使用lightweight网络，虽然效率提高了，但是准确率令人担忧.  
本文的方法使用一种分级的结构.和RefineNet不同，RefineNet主要强调在一次foward pass中通过不同层的特征融合来提高性能，而本文的级联网络采用级联图片作为输入来加速推理和构建实时SS.  

# Speed Analysis
主要分析了PSPNet速度慢的缺点的原因，并进行改正.  
经过分析发现，图片分辨率是影响速度的最主要的因素. 同时，发现网络中kernel的数量也是一个重要的因素（基本和分辨率相当）.  
作者尝试了三种方法：下采样图片分辨率、下采样特征max-pooling、模型压缩减少kernel，但是效果都不好.  
![0](http://i1.piimg.com/589172/bbc08335796850b0.png)  
![1](http://i1.piimg.com/589172/df3fdeccc8110452.png)  
![2](http://i1.piimg.com/589172/efcc0f5d844ecdd6.png)  


# ICNet
针对以上的分析，发现，低分辨率的图片能够有效降低运行时间，但是失去很多细节，而且边界模糊；但是高分辨率的计算时间难以忍受，于是提出了下边的方法:  
![1](http://i1.piimg.com/589172/ab31c75dd90eae22.png)  
<br/>
采用低中高三种分辨率的图片协助进行语义分割.融合部分使用级联特征融合单元(CFF). 同时，使用级联标签监督来更有步骤地进行学习.  
值得注意的是，低分辨率分支超过50层，提取更多的语义信息(inference 18 ms)，中分辨率分支有17层conv，但是由于权重共享，只有inference 6ms，而高分辨率分支是3 conv，有inference 9ms.  
**与其他网络的不同**  
之前的那些方法，如FCN、SegNet、UNet、RefineNet等，强调单尺度或者多尺度输入的不同层的特征融合，所有的数据需要在整个网络中运行，因为高分辨率的输入而导致了昂贵的计算费用.而本文的方法，使用低分辨率图片作为主要输入，采用高分辨率图片进行refine，保留细节的同时减少了开销.  

# Cascade Feature Fusion and Final Model  
![1](http://i4.buimg.com/589172/3e35f4bcaed944e9.png)  

融合之后，对Loss函数进行了修正，`L = aL1 + bL2 + cL3`.  
最终，又对模型进行了压缩，没有采用那些经典的方法，而是使用了一种简单的方法：如果要保留1/2的权重，则先保留3/4，然后进行微调，然后再3/4，微调多次，步进达到目的.(同时，使用了引文[13]的方法，这里看的不是特别懂，之后学习一下13).  

# Experimental Evaluation
框架使用的是Caffe，网络结构基于PSPNet，将金字塔池模块中的并置操作改为求和，因此特征长度从4096减少到2048.  
<br/>
最后的结果:  
![1](http://i1.piimg.com/589172/d3a9997a73fa2179.png)  


# References
* [1] SegNet
* [2] deeplabv1
* [3] deeplabv2
* [13] Pruning filters for efficient convnets
* [14] Refinenet: Multi-path refinement networks for high-resolution semantic seg-
mentation
* [17] Ssd: Single shot multibox detector.
* [18] Semantic image segmentation via deep parsing network
* [19] FCN
* [20] DeconvNet
* [21] Enet: A deep neural network architecture for real-time semantic segmentation.
* [24] YOLO9000: better, faster,
stronger
* [25] Faster R-CNN: Towards real-time object detection with region proposal networks
* [32] Multi-scale context aggregation by dilated convolutions
* [33] Pyramid scene parsing network 2017
* [34] crfasrnn

# 相关资料
* 最初读这篇文章是看到知乎专栏推送的：https://zhuanlan.zhihu.com/p/26653218?group_id=842085390016974848  
* 源代码(现在还没放，晚点可能会放在这里)：https://github.com/hszhao/ICNet
* 一个视频样例：https://youtu.be/qWl9idsCuLQ
