deeplab有两篇论文，由于第二篇是在第一篇上增加了一部分内容，就放在一起进行学习了.
<br/>
# 第一篇  
Semantic Image Segmentation with Deep Convolutional Nets and Fully Connected CRFS  
<br/>
# 基本信息
这篇是ICLR2015上的一篇文章，所属领域为semantic segmentation.
<br/>
# Abstract
我们发现在DCNN的最后一层的响应没有被足够的定位用于准确的对象分割.这是因为不变性质使DCNNs对high-level任务好.   
我们通过在DCNNs的最后一层连接一个fcCRFs克服这个poor localization.  

# Introduction
DCNNs的成功可以部分归因于DCNN对局部图像变换的内在不变性，这支持了他们学习数据层次抽象的能力.但是这个不变性对height-level tasks有好处，却妨碍了low-level tasks，例如semantic segmentation.在这类任务中，我们期望精确的定位，而不是空间信息的提取.  
**DCNNs用于语义分割的两个困难(downsampling,invariance)**  
(1)涉及在标准DCNN的每一层执行的max-pooling和downsampling（“striding”）的重复组合引起的信号分辨率的降低.对于这个问题本文使用'atrous(with holes)'算法，这个算法最初是用于非抽样离散小波变换.这使得DCNN响应的有效密集计算方案比早期解决该问题的方案简单得多.(2)第二个问题涉及从分类器获取面向对象的决策需要对空间变换的不变性，固有地限制了DCNN模型的空间精度.这里使用fcCRFs解决.  
**DeepLab的三个优点**  
(1)speed,通过atrous(2)精度(3)简单  
<br/>
# Related Work
早期的两阶段方法通常使用自下而上的图像分割和基于DCNN的区域分类的级联，前端的分割会存在很大的潜在错误.  
<br/>
# CNN for dense image labeling
deeplab把在Imagent上与训练的vgg16分类网络作为一个高效的dense feature extractor，来用于图像语义分割系统.  
**使用hole算法的 efficient dense sliding window 特征提取器**  
本文转化vgg16的最后两层成为conv，但是这是不够的，因为网络的产出非常稀疏的计算检测分数（步长是32）.期望的目标步长是8，因此本文跳过最后两次的max-pooling并修改跟着这两层的conv filter，通过引入0来增加filter的大小，分别是最后三层conv是2x，第一个fc是4x.其实，本文的做法是使conv filter保持不变，令input-stride是2或者4.这个方法叫“hole algorithm”(atrous algorithm)最初是用于ndecimated wavelet transform的.实现上只是修改im2col文件，增加选项用于对bottom层的稀疏采样.  
这里的损失函数是 **cross-entropy** .  
由于atrous network产生的结果比较光滑，所以直接使用系数为8的二次插值还原到原图像（FCN使用的是需要学习的upsampling layer，原因是产生FCN产生的结果比较粗糙），减少很多计算量.  
**控制感受野并加速卷积网络的稠密计算**  
本文的方法可以精确的控制感受野的尺寸.通过把第一个fc-conv层filter变为4x4，使得感受也缩小为128x128.并且较少了2-3倍的运行时间.  
<br/>
# fcCRF和多尺寸预测
DCNN score map很适合预测可以可靠地预测图像中对象的存在和粗略位置，但不太适合用于指向其精确轮廓.原因是多层max-pooling已经被证明增加不变性和大的感受野，会导致从score map中预测位置比较困难.  
解决这个问题，一个方法是利用multi-layers信息，另一个方法是采用超像素表示，本质上是将本地化任务委托给低级分割方法（这个地方不太明白）.
**fcCRFs**  
这里先使用fcCRFs解决定位问题.  
CRFs很早已经被用来光滑分割图片的噪声，本质上是用short-range CRFs函数来清除那些基于local hand-engineered features的弱分类器的不正确预测.但是在本文的方法中，已经得到了十分smooth的结果，如果贸然使用CRFs只会对结果又有害，因为本文需要的是recover detailed local structure而不是smooth.于是我们采用了fcCRFs.（fcCRFs可以参考我的另一篇文章）  
**Multi-scale prediction**  
本文为了提高定位精度，也使用了一种multi-scale的方法，在前四层的每个max-pooling层的输出后加上一个两层的MLP连接到网络的最后一层进行融合.  
当然，这个效果是没办法和fcCRFs比的.  
<br/>
接下来的实验具体细节可以参考原论文.  

# 第二篇
DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs

# 主要改进  
**重新明确使用DCNNs进行语义分割的三个挑战**  
(1)特征的分辨率减小(2)目标可能在不同尺度下(3)DCNN的不变性导致定位的精度降低.  
其中(1)(3)在第一篇文章中已经论述过了，挑战(1)使用atrous conv + 线性插值，挑战(3)使用fcCRFs，主要改进是提出了挑战(2)，引入了ASPP atrous spatial pyramid pooling，相比还有一种方法是skip-layers ，从多层提取出hyper-column features.

# 相关资料
* 参考：http://blog.csdn.net/yxq5997/article/details/53693869
* 参考：http://www.dongzhuoyao.com/deeplab-semantic-image-segmentation-with-deep-convolutional-nets-atrous-convolution-and-fully-connected-crfs/
* http://blog.csdn.net/chenyj92/article/details/53448161 这篇文章感受野部分和我理解的一样，与论文中不同.
* 项目主页（包括源代码）：http://liangchiehchen.com/projects/DeepLab.html
