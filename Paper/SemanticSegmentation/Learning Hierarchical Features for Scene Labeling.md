# 基本情况
这是PAMI2013的一篇文章，作者是LeCun等人，所属领域是Image Segmentation.

# Abstract
本文提出了一种多尺度CNN，并且结合超像素的最佳覆盖，实现语义分割。在Sift Flow（33类）和Barcelona DataSet （170类）打破记录，在Stanford Background Dataset（8类）接近记录。产生320 ×240图像标签不到一秒钟。

# 两个问题  
在场景解析的背景下，有两个主要的重要问题：如何产生视觉信息的良好内部表示，以及如何使用上下文信息来确保解释的自我一致性.  本文的主要使用深度学习的方法解决上述的两个问题，主要想法是在一个大输入窗口上使用卷积网络操作产生每个像素位置的标签预测.卷积神经网络本身通过多个阶段的卷积、非线性激活、空间pooling来实现end-to-end的训练，从而自动学习分级特征表示.  
但是，通过一个小的区域（卷积核大小）来标注每个像素比较困难.因为，一个像素的分类可能有的时候依赖于相对short-range的信息，例如人脸的存在可能暗示人身体的存在；来有的时候需要依赖long-range的信息，确定一个像素属于公路需要大范围的信息；为了解决这个问题，本文提出了使用multi-scale卷积神经网络.  
<br/>  
经典的分割方法一般是先使用基于图的方法产生分割的侯选块，然后使用engineered特征进行对候选分割区域的编码.最后使用CRF或者其他的图模型训练来产生每个候选块的标签，来保证标签的全局一致性.本文通过大的上下文窗口可以不使用复杂的后处理且能确保标签一致性.  

# 框架
本文提出的方法架构如下图所示:  
![1](https://user-images.githubusercontent.com/16068384/35631439-dd79feee-06de-11e8-9829-62aae0d63179.png)
上述架构主要由两部分组成:  
(1)Multi-scale卷积表示.不同的尺寸对应的网络是权值共享的，其实是同一个网络的copy，输入的图片是输入图片的Laplacian pyramid的不同尺寸.这种方法可以被学习被高效的进行场景中的物体和区域的检测和识别，但是无法找到区域的精确边界，因此需要后处理来勾勒.  
(2)Graph-based classification.  
考虑了三种方法来产生最终的图片标注:1.Superpixels.通过在卷积特征向量上训练pixelwise分类器，使用简单的投票方法来指定每一个superpixles的标签.这种方法是fixed-level，因此效果不太理想.(2)CRF over superpixels.在superpixel基础上使用CRF，避免判别结果超出常规.但是这种对本文来说不是必须的，因为multiscale feature使得大多数的scene-level关系已经被捕捉到了.(3)Multilevel cut with class purity criterion.也就是使用一族的方法方法进行分割,比如同一方法使用不同参数等.
<br/>

# 总结
本文使用多尺度的CNN进行语义分割，这是目前比较常用的做法。但是，在作者看来，  `逐像素分类的精度无论如何都是不准确的，识别稀有的物体往往比精确标注天空的每一个边界的像素更重要`。  
　　