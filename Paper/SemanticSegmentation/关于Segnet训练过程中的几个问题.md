### 环境
操作系统: ubuntu14.04  
caffe: caffe-segnet(官方)  
model: segnet-Tutorial  

### 需要注意的问题
1. 比较segnet_model_driving_webdemo.prototxt和segnet_inference.prototxt发现，只有卷积的权重初始化方式（w和b）和最后一层不同(webdemo为'argmax'而前者为'softmax').  
2. 由于官方的segnet model zoo只提供了部分训练好的权重，并且一些权重存在问题(例如segnet_basic_camvid.caffemodel只有5.7M，以及bayesian_segnet_basic_camvid.caffemodel也只有6M)，而论文中说segnet的模型大小是117M，说明caffemodel上传的应该是错误的.结合问题1，暂时就使用webdemo的caffemodel进行测试.  
3. segnet和webdemo的识别类别是不一样的，前者是11，后者是12；别切不同类别的所使用的颜色表示也是不一样的.所以需要如果使用webdemo的caffemodel对test_segmentatino_camvid.py进行预测，需要添加预测部分的颜色.可以参考`https://github.com/alexgkendall/SegNet-Tutorial/issues/51`.  
4. 关于如果使用webdemo进行预测，还需不需要进行batch normalization.测试了一次发现，不能使用batch normalization,如果使用bn对webdemo.caffemodel进行处理，结果变得很差.以下分别是不使用bn和使用bn获得的结果.  
![1](http://i1.piimg.com/589172/dc6b23d3fd8fccff.png)  
![2](http://i1.piimg.com/589172/1a1e4cf292992ed1.png)  
5. 自己使用cityscapes的数据集进行了训练，在vgg16上进行finetune，使用cityscapes-fine数据，resize到480x240.训练了将近100轮，相关结果之后会记录.
