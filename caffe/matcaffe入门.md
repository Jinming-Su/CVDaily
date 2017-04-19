### 参考资料
* matcaffe安装到使用.http://caffecn.cn/?/page/tutorial (http://blog.csdn.net/ws_20100/article/details/50525879)
* http://blog.csdn.net/gybheroin/article/details/54177436

### 环境
* ubuntu 14.04
* caffe最新版(github)
* matlab R2016b

### 从失败到成功
* 话说，我的matcaffe安装过程也是一波三折，最开始的时候就参考这篇文章，caffe中文社区教程http://caffecn.cn/?/page/tutorial ，参考6.3节是matcaffe的官方教程。有个人单独把这一节转载到csdn blog上了，http://blog.csdn.net/ws_20100/article/details/50525879 .
* 最开始照着这个教程做，使用的matlab R2014a，结果一直出问题，问题是每次获取solver进行执行solver.solve()都会导致matlab卡死；有时会还会提示MEX file存在异常，xxx各种奇怪的操作。
* 之后，google了好久，发现上述问题十分普遍，有人说他通过花了一个版本的caffe解决了这个问题。于是我的想法是，caffe是最新版的(github)，没有必要进行更换，就在6v上下载了一个最新版的matlabR2016b。安装matlab过程也遇到了一些问题:(1)有两个.iso文件，需要分两步安装，每步挂载一个iso（2）安装时候，不能在挂载的文件系统内进行安装。之后对matcaffe重新进行了编译，编译过程没有任何错误，结果程序运行起来了，nice。
* 实例运行结果  
  ![1](https://cloud.githubusercontent.com/assets/16068384/23211979/7c02ca0e-f93f-11e6-90b9-612765b2e6ed.png)
