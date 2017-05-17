# 推荐资料
* 强烈推荐这篇文章：贾扬清：希望Caffe成为深度学习领域的Hadoop  http://www.csdn.net/article/2015-07-07/2825150 .贾扬清阐述了caffe的诞生过程，从中可以看出他的成才之路，一个做什么都思路非常清晰的人.  
* 推荐这篇文章：Caffe 作者贾扬清：我为什么离开 Google，加入 Facebook.
* caffe的在线分类Demo: http://demo.caffe.berkeleyvision.org/
* caffe model zoo
* ethereon
* caffe tutorial  
中译本可以从这里获取：http://caffecn.cn/?/page/tutorial
* Caffe for Python: http://blog.csdn.net/jnulzl/article/details/52077915

<br/>
<br/>

这篇文章是CVPR 2015的文章.主要介绍了Caffe的亮点和架构.  
创造Caffe的原因主要是为了让研究人员和从业人员能够方便的使用深度神经网络.推荐看一下推荐资料中的第一篇文章，文中贾扬清讲解了创作caffe的初衷和创作过程.  

# HightLight of Caffe
(1) 模块化.能够方便地扩展数据格式、网络层、损失函数等.  
(2) 表示与实现分离.Caffe model 使用Protocol Buffer语言进行定义，易读易懂形式化，高效序列化，且有多种语言的实现接口，尤其是C++和Python.  
(3) 测试覆盖. 每个模块的代码都进行了测试（这部分感觉没必要写...）.  
(4) Python 和 Matlab 借口.  
同时，和其他的CNN软件比起来，有两个优点：一个是完全使用C++实现，很容易集成到C++系统中；提供了微调的功能.  
