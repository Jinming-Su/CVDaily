---
title: FCN的deconvolution
date: 2017-03-26 00:00:01
categories:
- Deep_Learning
- caffe
tags:
- deconvolution
- transposed_convolution
description: 反卷积（转置卷积该如何计算）
---

### 参考  
* https://github.com/vdumoulin/conv_arithmetic  

### FCN中的反卷积过程  
#### 在 fcn32s 上进行测试
**Deconvolution:** 先对 fcn32s 进行说明，输入的是一个 500 * 500 的图片， Deconvolution 层的输入尺寸是 16 * 16 * 21, 转置卷积的参数是 {64 * 64 * 21 * 21, stride = 32}. 转置后的结果是 544 * 544 * 21 * 1.对以上转置卷积过程进行推算，最后得出一种合适的过程是: (63 + 15 * 32 + 1 + 63 - 64) / 1 + 1 = 544.  

#### 在 fcn16s 上进行测试  
**pool4:** 同样拿 500 * 500 的图片在 fcn16s 上进行测试，pool4 的输出尺寸是 (1, 512, 44, 44), pool4的一个分支经过score_pool4层的卷积，得到尺寸是 (1, 21, 44, 44).  
**deconvolution:** 另一个分支经过score_fr层的卷积，得到尺寸是 (1, 21, 16, 16), 继续进行Deconvolution，参数是{4 * 4 * 21* 21, stride = 2}， 得到尺寸是 (1, 21, 34, 34). 对以上转置卷积过程进行推算，得到过程是: (3 + 15 * 2 + 1 + 3 - 4) / 1 + 1 = 34.  
**crop:** 然后把前一个blob以后一个blob为参照进行 **Crop** ，经过score_pool4c得到的尺寸是 (1, 21, 34, 34).  
**fuse(Eltwise):** 在fuse_pool4层进行两个尺寸是(1, 21, 34, 34)的求和, 尺寸仍然是(1, 21, 34, 34).  
**再次 Deconvolution** : upscore16的参数是{32 * 32 * 21 * 21, stride = 16}, 依照之前得到的规律，输出尺寸应该是: (31 + 33 * 16 + 1 + 31 - 32) / 1 + 1 = 560.总的尺寸参数是(1, 21, 560, 560)  
**Crop**: 重新切割会500
