---
title: 【fcCRFs】Efficient Inference in Fully Connected CRFs with Gaussian Edge Potentials笔记
date: 2017-04-16 00:00:01
categories:
- Deep_Learning
- Paper
tags:
- fcCRFs
description: fully connected conditional random fields
---

### 基本情况
* time: 2011NIPS, CVPR2012
* domian: segmentation

### Abstract
* 目前，大部分state-of-the-art的多类别图像分割算法都使用基于像素或者区域的CRFs.虽然区域级别模型通常具有密集的成对连接性，但像素级模型相当大，只允许使用稀疏图形结构.
* 本文的主要贡献是对于fc CRFs的高效近似推理算法，其中pairwise edge potential使用高斯核的线性组合定义.

### Instroduction
* 在处理segmentation任务是，常见的方法是将这个问题作为在像素或图像补丁上定义的条件随机场（CRF）中的最大后验（MAP）推理.CRF势能包含了使相似像素之间的标签一致性最大化的平滑度项，并且可以整合更精细的项目，以模拟对象类之间的上下文关系.
* Basic CRF由基于单个像素或者图片块的一元势能和基于相邻pixedl或patches的pair-wise势能组成.所产生的相邻CRF结构在图像中建立长距离连接的能力受到限制，并且通常导致对象边界的过度平滑.有人将basic CRF扩展到基于图片region的高阶potential.但是这种方法的精度严重依赖于unsupervised image segmentation( 用于compute the regions on which the model operates) 
* 本文的主要贡献就是建立了一个高效的fc CRFs模型推理算法，算法是基于平均场近似成CRF分布.
* 所得到的近似推理算法在模式中的边缘数量上是亚线性的.

### The fc CRF Model
* 这部分公式比较多，详细看论文

### Efficient Inference in Fully Connnected CRFs
* **KL divergence**  
(参考:http://blog.csdn.net/gao1440156051/article/details/44162269)
在概率论或信息论中，KL散度( Kullback–Leibler divergence)，又称相对熵（relative entropy)，是描述两个概率分布P和Q差异的一种方法。它是非对称的，这意味着D(P||Q) ≠ D(Q||P)。特别的，在信息论中，D(P||Q)表示当用概率分布Q来拟合真实分布P时，产生的信息损耗，其中P表示真实分布，Q表示P的拟合分布.
* **平均场近似CRF**  
![1](https://cloud.githubusercontent.com/assets/16068384/25065281/a8b85522-223f-11e7-964a-836f5519a0db.png)  
瓶颈在于message passing.由于需要计算每个i和每个j关系，所以朴素算法的时间复杂度是O(N^2).  
* 使用高维过滤(转化为卷积的过程)  
![2](https://cloud.githubusercontent.com/assets/16068384/25065280/a8b7434e-223f-11e7-8604-83d8fcd9cc84.png)  
实现了O(N)的时间复杂度.

### 源代码
* https://github.com/lucasb-eyer/pydensecrf
* https://github.com/johannesu/meanfield-matlab.git 
* 可以参考的文章: http://www.jianshu.com/p/434b3e22a47e
* 我之前也写过一篇CRF入门 https://github.com/su526664687/Articles/blob/master/Deep_Learning/CRF%E5%85%A5%E9%97%A8.md
