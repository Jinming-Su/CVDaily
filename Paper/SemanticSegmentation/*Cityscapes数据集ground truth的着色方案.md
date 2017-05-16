训练过程中只使用19类，其Ground truth使用灰度图表示，为了显示方便官方提供了color的图像.颜色自己提取了一下，分别如下: 
```
0 ROAD = [128, 64, 128]
1 SIDEWALK = [244, 35, 232]
2 BUILDING = [70, 70, 70]
3 WALL = [102, 102, 156]
4 FENCE = [190, 153, 153]
5 POLE = [153, 153, 153]
6 TRAFFIC_LIGHT = [250, 170, 30]
7 TRAFFIC_SIGN = [220, 220, 0]
8 VEGERATION = [107, 142, 35]
9 TERRAIN = [152, 251, 152]
10 SKY = [70, 130, 180]
11 PERSON = [220, 20, 60]
12 RIDER = [255, 0, 0]
13 CAR = [0, 0, 142]
14 TRUCK = [0, 0, 70]
15 BUS = [0, 60, 100]
16 TRAIN = [0, 80, 100]
17 MOTOCYCLE = [0, 0, 230]
18 BICYCLE = [119, 11, 32]
255 OTHER = [0, 0, 0]
```  
其中，第一列表示灰度值（ground truth的标注），第二列是分类和在color图像的rgb值（ground truth color的标注），255在测试时不计算，通常在训练过程中不计入loss.
