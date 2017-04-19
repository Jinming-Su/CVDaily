### cs231n notes
* lecture 1 介绍计算机视觉
    * 生物视觉的起源从5.4亿年前的物种大爆发开始--眼睛的出现是物种多样性迅速增多的一个重要因素.
    * 早期计算机视觉研究的两大结论：视觉的前期功能是识别边缘和简单的形状；视觉功能是分层的（影响了后来包括深度学习分层在内的很多研究）
    * 计算机视觉的两大研究领域：3D建模；图像识别（主流）
    * 计算机视觉当前的两大愿景：看图写作；视觉智能（视觉理解，涵盖文化范畴）
* Lecture 2 线性分类
    * 曼哈顿距离：又称L1距离，对应坐标的差的绝对值之和
    * KNN(k-NearestNeighbor)，见https://github.com/su526664687/Articles/blob/master/deep_learning/knn.md
    * SVM
    * softmax分类（一般化的logistic回归）,参考http://blog.csdn.net/xbinworld/article/details/45291009 
* Lecture 3 误差比较和优化
   * 梯度下降法
   * 学习率问题：通常开始使用大的学习率，之后对学习率慢慢减小
* Lecture 4 反向传播和简单神经网络
   * 反向传播常用模式
      * add gate: 梯度分配器——两边梯度相等
      * max gate: 梯度路由——最大值梯度看做1，小值梯度看做0
   * 常用激活函数
      * 在机器学习历史上，最早使用tanh函数
      * 2012年，ReLU(修正线性单元) max(0,x)开始流行【当今的默认选择】
      * 最近，leaky ReLU, Maxout ELU
   * 计数神经网络层数是计算有权值的层数， 输入层并不计算在内
   * http://cs.stanford.edu/people/karpathy/convnetjs/demo/classify2d.html 在线二分类二层神经网络测试
   * 加入适当的正则化参数，可以防止过拟合问题
* Lecture 5 训练神经网络细节
   * 使用CNN进行迁移学习
      * 首先，在大数据集上进行预训练（如ImageNet），这个已经有许多人做好了，可以利用pre training好的模型，比如Caffe Model Zoo的。CNN当做一个特征提取器进行对待
      * 其次，finetune自己的own data.如果数据量比较小，只需要训练分类器就可以了；如果数据量比较大，可以训练部分网络或者整个网络。
   * 激活函数
      * 上一节已经提到了很多的激活函数
      * 历史上最常使用的激活函数是sigmoid函数，存在许多问题
         * 1. [梯度弥散或者梯度消失]：sigmoid处理的神经元会成为一个饱和神经元（输出存在极限），输出要么为0，要么为1，导致反向传播中出现梯度趋向于0
         * 2. sigmoid输出值不是中心对称的
         * 3. exp()计算耗时
      * tanh()为了改进sigmoid而提出来的，解决了中心对称问题
      * ReLU在2012年被提出，成为一种默认使用的激活函数，在x>0区域解决了sigmoid的饱和问题，但是存在问题
         * 1. 不是中心对称
         * 2. x<0区域存在梯度弥散(dead ReLU)
      * Leaky ReLU(max(ax, x))/ELU/Maxout   
      ![1](https://cloud.githubusercontent.com/assets/16068384/23091672/523b698e-f5f6-11e6-86ae-9c63172255f0.png)
   * 数据预处理
      * 图像处理的数据预处理  
      ![1](https://cloud.githubusercontent.com/assets/16068384/23093337/4a7eab82-f61b-11e6-8a03-7086c5fc6771.png)
   * 权重初始化
      * 根据对称性，初始化的时候如果weight不随机那训练出来的weight就都一毛一样了
      * 随机化常采用的是N(0,0.01)，关于不同的激活函数，tanh和ReLU等初始化形式不同
   * 批处理正则化（这种方法可以省去考虑权重初始值问题）
   * 学习过程
      * 交叉验证
   * 超参数优化
* Lecture 6 训练神经网络细节
   * 参数更新
      * SGD最慢
      * momentum(v = mu * v - lr * dx; x += v)
      * Nesterov Momentum(先用更新后的位置的梯度)  
      ![1](https://cloud.githubusercontent.com/assets/16068384/23098737/27c5b768-f691-11e6-9838-e3dc58261c70.png)
      * adaGrad 梯度大的抑制一下步长, RMSProp优化adaGrad
      * Adam： momentum + RMSProp[默认比较好的选择]
   * regularization: dropout
      * 前向传播的时候，随机把一些神经元置0，反向传播同样进行
      * 作用：防止过拟合
      * test的时候可以多次dropout采样求平均,但是效率比较低（Monte Carlo approximation）。另一种方法就是，不进行dropout（神经元失活），而是在输出过程中对输出值乘以一个概率P（P的值与神经网络的结构有关）
* Lecture 7 CNN细节
   * CNN例图  
   ![1](https://cloud.githubusercontent.com/assets/16068384/23103275/c8a03ca0-f6f3-11e6-8d2e-060db225ad0f.png)
   * CNN特点：局部感知；参数共享（全图同一个卷积核）；
   * 卷积层 http://blog.csdn.net/real_myth/article/details/51824193
      * 滤波器就是卷积核
      * 步长stripe, 填充padding
   * pool层 下采样（down sampling）
      * conv层通常不会在空间上减小数据的size，而是保持数据的size,通常是在下采样层减小数据的尺寸
      * 常见方式： max pooling（在一个滤波器范围内取最大值）; average pooling
   * fc全连接层
   * http://cs.stanford.edu/people/karpathy/convnetjs/demo/cifar10.html 在线CNNjs训练
* Lecture 8 迁移学习之物体定位和检测
   * 定位一般是一个对象，而检测通常是多个对象
   * 引用csdn上的一段话：  
      * 1.对于分类而言，就是对于给定的图片把其划分到给定的几种类别中某一种。很显然，图像中只能存在一种给定类别中的对象。 
      * 2.而定位就是找到对应的对象的位置区域，把它框选出来（即Bounding Box），这个选框除了位置信息（x，y）外还要包含其大小信息（w，h）。同样的，这里的图像只包含单个对象。 
      * 3.检测就可以看作是定位的拓展，即给定一张图像或者视频帧，找出其中所有目标的位置，并给出每个目标的具体类别。与定位的不同就是图像中包含的对象数不确定。 
      * 4.实例分割（Instance Segmentation），就是在检测的基础上，把每个对象的轮廓勾勒出来，随之而来的就是语义分割（Semantic segmentation）
   * 定位分为不定类和定类定位两种
      * 一种方法是使用全连接训练一个回归网络，进行定位
      * 另一种方法通常采用一种sliding windows: overfeat的方法，最后进行聚类的方法进行合并, 高效的滑动窗口overfeat会把fc层转化为conv
   * 检测(参考资料：http://blog.csdn.net/qq_30159351/article/details/52440058)
      * Region Proposals： 选取比较可能包含图像的部分进行检测
         * 比较出名的方法是：Selective Search： 首先将图片打散，然后按照超像素的原理（superpixel），根据人为定义的距离进行聚合。   
         ![1](https://cloud.githubusercontent.com/assets/16068384/23113918/7e31572a-f776-11e6-86f1-1dbf45b4fb44.png)
         * R-CNN
            * 1 训练一个分类模型
            * 2 微调模型用于检测问题
            * 3 利用selective search算法在图像中提取2000个左右的region proposal, 将每个region proposal缩放（warp）成227x227的大小并输入到CNN，将CNN的fc7层的输出作为特征。 
            * 4 将每个region proposal提取到的CNN特征输入到SVM进行分类。 
            * 5 对于SVM分好类的region proposal做边框回归（bounding-box regression)，边框回归是对region proposal进行纠正的线性回归算法。
            * 存在问题: 1.运行速度慢 2.训练分为多个阶段，步骤繁琐 3.支持向量机和回归是事后训练的：CNN特征没有根据支持向量机和回归来更新 
          * fast-RCNN  
          ![1](https://cloud.githubusercontent.com/assets/16068384/23114655/49e54f76-f77b-11e6-80b5-bc40b1f2cff5.png)
          * faster-RCNN
            * 采用RPN(Region Proposal Networks).RPN的核心思想是使用卷积神经网络直接产生region proposal，使用的方法本质上就是滑动窗口。RPN的设计比较巧妙，RPN只需在最后的卷积层上滑动一遍，因为anchor机制和边框回归可以得到多尺度多长宽比的region proposal。 
      * 目前，最好的水平是ResNet101 + R-CNN + some extras
      * YOLO
* Lecture 9 CNN可视化
   * t-SNE 一个数据可视化工具
   * deep dream
   * fool CNN
* Lecture 10 RNN 
   * LSTM(Long short Term Memory) http://www.jianshu.com/p/9dc9f41f0b29
* Lecture 11 
   * CNN训练过程中主要问题  
   ![1](https://cloud.githubusercontent.com/assets/16068384/23129169/95ee4e04-f7bc-11e6-94b4-1ed3a1371ea0.png)
   * Data Augmentation(目的是为了防止过拟合，dropout和dropconnect也可以达到这样的效果[训练时添加噪声，测试时弱化噪声])
      * 1 最简单的方法是: 对图片横向翻转
      * 2 随机截图（大小和位置随机).这种方法常采用的一种形式是左上、右上、左下、右下、中间截图5张，然后进行翻转，一共10张图
      * 3 颜色变动：　常用的是PCA
      * 4 任意的方法的组合：　移动、旋转、伸缩、放射等
   * Transfer Learning(目的：有时候新的领域没有太多的数据用于训练CNN，可以把在其他领域训练好的CNN模型拿来使用)  
   ![1](https://cloud.githubusercontent.com/assets/16068384/23131155/009353d8-f7c4-11e6-828d-36072b7b90f6.png)
   * How to stack conv
      * 把大的conv分解成多个小的conv表现更好, 可以减少很多参数,减少计算量.
      * 注意： 把卷积层分解成不对称的卷积层现在用的还不多.
