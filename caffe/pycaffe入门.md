---
title: pycaffe入门
date: 2017-03-22 00:00:01
categories:
- Deep_Learning
- caffe
tags:
- pycaffe
description: ...
---

### 参考
* Caffe for Python 官方教程(翻译)  http://blog.csdn.net/jnulzl/article/details/52077915
* Caffe均值文件mean.binaryproto转mean.npy http://blog.csdn.net/hyman_yx/article/details/51732656

### 实例
* **说明** ： 以下例子是针对alexnet的
* Caffe均值文件mean.binaryproto转mean.npy
  
  ```python 
  #coding=utf-8
  import caffe
  import numpy as np

  MEAN_PROTO_PATH = 'data/imagenet_mean.binaryproto'               # 待转换的pb格式图像均值文件路径
  MEAN_NPY_PATH = 'data/mean.npy'                         # 转换后的numpy格式图像均值文件路径

  blob = caffe.proto.caffe_pb2.BlobProto()           # 创建protobuf blob
  data = open(MEAN_PROTO_PATH, 'rb' ).read()         # 读入mean.binaryproto文件内容
  blob.ParseFromString(data)                         # 解析文件内容到blob

  array = np.array(caffe.io.blobproto_to_array(blob))# 将blob中的均值转换成numpy格式，array的shape （mean_number，channel, hight, width）
  mean_npy = array[0]                                # 一个array中可以有多组均值存在，故需要通过下标选择其中一组均值
  np.save(MEAN_NPY_PATH ,mean_npy)
  ```
* 测试实例
  
  ```python
  #coding=utf-8
  import numpy as np
  import matplotlib.pyplot as plt
  import caffe
  import timeit

  #************************** set display parameters
  plt.rcParams['figure.figsize'] = (10, 10)        # 图像显示大小
  plt.rcParams['image.interpolation'] = 'nearest'  # 最近邻差值: 像素为正方形
  plt.rcParams['image.cmap'] = 'gray'  # 使用灰度输出而不是彩色输出

  #************************** set networks
  caffe.set_mode_cpu()

  model = 'deploy.prototxt'
  weight = 'data/bvlc_alexnet.caffemodel'
  net = caffe.Net(model, weight, caffe.TEST)

  #************************** set preprocessor
  # 加载ImageNet图像均值 (随着Caffe一起发布的)
  mu = np.load('data/mean.npy')
  mu = mu.mean(1).mean(1)  #对所有像素值取平均以此获取BGR的均值像素值
  print 'mean-subtracted values:', zip('BGR', mu)

  # 对输入数据进行变换
  transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})

  transformer.set_transpose('data', (2,0,1))  #channel 放在前面
  transformer.set_mean('data', mu)            #对于每个通道，都减去BGR的均值像素值
  transformer.set_raw_scale('data', 255)      #将像素值从[0,255]变换到[0,1]之间
  transformer.set_channel_swap('data', (2,1,0))  #交换通道，从RGB变换到BGR

  #************************* test
  net.blobs['data'].reshape(50,        # batch 大小
                        3,         # 3-channel (BGR) images
                        227, 227)  # 图像大小为:227x227

  image = caffe.io.load_image('data/cat.jpg')
  transformed_image = transformer.preprocess('data', image)
  # plt.imshow(image)
  # plt.show()

  # 将图像数据拷贝到为net分配的内存中
  net.blobs['data'].data[...] = transformed_image

  # 执行分类
  output = net.forward()  
  output_prob = output['prob'][0]  #batch中第一张图像的概率值   
  print 'predicted class is:', output_prob.argmax()

  # 显示中文分类结果 
  labels_file = 'data/synset_words.txt'
  labels = np.loadtxt(labels_file, str, delimiter = '\t')
  print 'output label: ', labels[output_prob.argmax()]
  # 查看前几的结果
  top_inds = output_prob.argsort()[::-1][:5]  # argsort函数返回的是数组值从小到大的索引值
  print 'probabilities and labels:', zip(output_prob[top_inds], labels[top_inds])
  ```
