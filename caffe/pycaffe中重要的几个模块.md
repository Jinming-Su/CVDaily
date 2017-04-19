---
title: pycaffe中重要的几个模块
date: 2017-03-25 00:00:01
categories:
- Deep_Learning
- caffe
tags:
- pil
- matplotlib
description: 介绍一下PIL, matplotlib.pyplot的使用
---

#### 参考资料  
* PIL http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140767171357714f87a053a824ffd811d98a83b58ec13000  
* matplotlib.pyplot http://blog.csdn.net/jasonding1354/article/details/42125555?utm_source=tuicool&utm_medium=referral


#### PIL
* 打开图片 `im = Image.open('test.jpg')`
* 获取图片尺寸 `im.size`
* 大小转化 `im.resize((w,h))`
* 缩放图片 `im.thumbnail((w//x, h//x))`
* 保存图片 `im.save('test.jpg', 'jpeg')`
* 其他功能还有切片、旋转、滤镜、输出文字、调色板等
* 模糊效果 `im2 = im.filter(ImageFilter.BLUR)`
* ImageDraw提供了一系列绘图方法

#### matplotlib.pyplot
* 画图 `plt.plot([x],[y],style), plt.show()`
* 坐标轴 `plt.axis([xmin, xmax, ymin, ymax])`
* 加文本说明 
    * `plt.xlabel('xxx'), plt.ylabel('xxx'), plt.title('xxx')`
