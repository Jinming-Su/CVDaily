# 引介
Liu W, Rabinovich A, Berg A C. Parsenet: Looking wider to see better[J]. arXiv preprint arXiv:1506.04579, 2015.  
图像语义分割的文章

# Abstract
本文展示通过一种技术添加global context到FCN中进行语义分割.具体方法是使用 global average pooling来加强每个位置的特征.同时，使用了一种学习归一化参数的方法.

# Introcuction
FCN抛弃了global信息，因此忽略了内在的有用的场景级别的语义上下文.deeplab等提出使用图模型的技术（例如CRF）引入global context and structured information到FCN中.  
本文提出了一种集成了global context的end-to-end（相对于基于patch的方法）的FCN方法，只是增加了少量的计算.  

# Related Work
早期的分割主要采用proposal+post-classification的模式，直到FCN的提出，本文也是基于FCN进行的实验.  
早期也有一些文章提到全局信息的重要性，CRF也是为了实现利用上下文信息，zoom-out利用上下文信息也得到了不错的结果.  

# ParseNet
### Global Context
理论上VGG的fc7应该有 404×404的感受野，但是本文用一个滑动的噪声去干扰输入图像，观察网络的输出，用来探测一个网络的有效感受野具体有多大，发现实际上只有图像的 1/4(原图500x500).  
![1](http://i4.buimg.com/589172/9ff16eae7e7fbfdd.png)  
实际的感受野太小了，没有足够的能力捕获global context.  
本文通过实验，使用一个Gobal Pooling可以显著特高感受野，也可以提升分割效果.  

### Early Fusion and Late Fusion
特征有两种融合方式，一个是早期融合，然后放入分类器一起分类，另一种就是晚期融合，就是分类后再融合.早期融合可以很好利用更多特征，晚期融合可能造成某些目标无法识别，仅仅是结合起来的情况.如果加入了L2正则，两者是相似的.  
做特征融合的时候一定要注意的是不同层的数据scale是不一样的，所以需要正则化才能融合.  

### L2 Norm Layer
尽管可以通过直接融合不同层，然后进行学习以改善不同scale的问题，但是这种方法仍然太过生硬，而且对于fine-tuning来说很难做好.所以本文提出使用 L2 norm，然后在对正则化后的数据进行scale.  

### Conclusion
本文认为精确证实了FCN不能提供足够的感受野，进而无法捕获足够的上下文信息，因此global context是需要的.  

### 相关资料
* ParseNet-caffe: https://github.com/weiliu89/caffe/tree/fcn
* model: caffe model zoo
