### 环境
* 项目地址 https://github.com/su526664687/caffe/tree/master/data/mine
* 实验平台 linux
* 参考 http://blog.csdn.net/gybheroin/article/details/54093619

### 准备
* 数据准备
* 把图片转化为lmdb
  http://www.cnblogs.com/denny402/p/5082341.html
  
    ```create_lmdb.sh
    #!/bin/sh
    rm -rf mtrainldb/ mvaldb/
    #../../build/tools/convert_imageset --shuffle \
    #--resize_height=256 --resize_width=256 \
    ../../build/tools/convert_imageset train/ train.txt mtrainldb

    #../../build/tools/convert_imageset --shuffle \
    #--resize_height=256 --resize_width=256 \
    ../../build/tools/convert_imageset val/ val.txt mvaldb
    ```
   
### 训练过程
* 训练
  
    ```train.sh
    #!/bin/sh
    ../../build/tools/caffe train --solver=lenet_solver.prototxt
    ```
* 训练过程存在的问题
  * 训练一开始, 一直存在Restarting xxx的问题，在重复获取数据，我认为可能是自己的过程存在问题，于是就再三检查自己过程，后来发现没有什么问题。重新浏览create_lmdb.sh文件的时候，发现在create_lmdb.sh文件中使用了较多的参数(不完全明白参数的含义)，于是把参数全部去掉，发现生成的ldb文件小了很多，就可以运行了。
* 测试（有两种方法）
  * 一种是采用批处理的方式进行测试
    
      ```
      #!/bin/sh

      ../../build/tools/caffe test --model=lenet_train_test.prototxt --weights=mine_iter_500.caffemodel 
      #mimg_mean.binaryproto catagory.txt val/11.bmp
      ```
  * 一种是采用采用classification.cpp的方法进行单个文件的测试
      
      ```
      #!/bin/sh

      ../../build/examples/cpp_classification/classification.bin \
      lenet_deploy.prototxt \
      mine_iter_500.caffemodel \
      mimg_mean.binaryproto \
      catagory.txt \
      0.jpg
      ```
