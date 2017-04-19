### 参考
* 测试fcn: http://www.cnblogs.com/xuanxufeng/p/6240659.html
* 训练fcn: http://blog.csdn.net/u013059662/article/details/51851797
* 安装pycaffe: http://m.blog.csdn.net/article/details?id=47624119
* 遇到错误ImportError: No module named skimage.io： http://www.cnblogs.com/empty16/p/4828476.html

### 环境
* ubuntu 14.04
* caffe最新版(github)
* matlab R2016b
* python2.7.6
* 项目地址： https://github.com/su526664687/caffe/tree/master/examples/fcn
* fcn： https://github.com/shelhamer/fcn.berkeleyvision.org
* voc2012: (镜像地址)https://pjreddie.com/projects/pascal-voc-dataset-mirror/

### 先测试
* 测试过程还好，不是特别的麻烦，参考文章http://www.cnblogs.com/xuanxufeng/p/6240659.html ,（这个地方才看到了infer.py） 由于主要使用matlab工具，特点是调试比较方便(python能不能方便地进行调试我现在还不知道，不过想到这里我有想玩eclipse写python了).
* <b>问题[需要解决]</b>： 测试结果没有python好，可能是matlab和python取值方法不一样，结果是matlab是灰度图，而python是非黑即白的图.
* 源码随后会进行分享
  
  ```
  clear
  clc

  addpath ../../matlab
  caffe.set_mode_cpu();
  % init_net
  deploy = 'voc-fcn8s/deploy.prototxt';
  caffe_model = 'voc-fcn8s/fcn8s-heavy-pascal.caffemodel';
  net = caffe.Net(deploy, caffe_model, 'test');

  im_data = imread('voc-fcn8s/test.png');
  im_data = single(im_data); 
  im_data = imresize(im_data, [500 500]);
  im_data = im_data(:, :, [3, 2, 1]); % 转换BGR
  im_data = permute(im_data, [2, 1, 3]); % flip width and height
  mean_data(:,:,1) = 104.00698793 * ones(500, 500); 
  mean_data(:,:,2) = 116.66876762 * ones(500, 500);
  mean_data(:,:,3) = 122.67891434 * ones(500, 500);
  im_data = im_data - mean_data;

  net.blobs('data').reshape([500 500 3 1]);
  net.blobs('data').set_data(im_data);
  net.forward_prefilled();

  [out I] = max(net.blobs('score').get_data(),[],3);
  imshow(permute(out, [2, 1, 3])/256);
  ```

### 再进行训练
* 训练过程就比较麻烦了，开始的时候我自己先写matlab的版本的,可是自己能力有限，就照着http://blog.csdn.net/u013059662/article/details/51851797 一步一步来。
* 第一步显然安装pycaffe依赖的包，如果安装教程的文章；下一步，由于我之前的版本没有在makeconfig中开启pythonlayer，所以对caffe进行了重新编译（话说，重新编译过程完成后，好像不需要在重新编译我之前编译过得matcaffe了）；下一步，pycaff安装过程可能有些许问题，参考顶部列出的文章；测试方法是在python中导入caffe不报错即可.
* 后来准备进行训练的过程才叫一个痛苦。师兄推荐使用pascal voc2012的数据集，花掉了我4个G的流量（校园网1元1g,这里要吹嘘一下东大的校园网，下载速度10m/s，不知道别的学校是不是）,但是使用的时候发现fcnvoc32s使用的2011的pascal voc.但是想到格式应该不变，就继续使用，然后下载两个caffermodel就1g多。。。
* 本来想着使用py就比较容易跑起来了,可是试了才知道，根本不是这回事。首先，py确实很多模块，需要把voc32s文件夹外部提供的模块copy进来，其次，发现train.prototxt第一层是python层（之前就提到过）,于是乎就去阅读了voc_layers.py，这个文件中定义了两个类（vocsegdatalayer和sbddsegdatalayer）作为连个python层中参数进行使用。这个文件最好都阅读一下，代码比较简单，注释也比较详细。之后就是改了一下参数，和一下路径（比如voc2011改成voc2012）.然后解决了一些比较简单的问题，于是就运行起来。（受宠若惊...）
