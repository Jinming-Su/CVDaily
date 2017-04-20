### 基本情况
这篇文章PASCALVOC官方发表在IJCV2015上的一篇文章，主要是对之前的2008-2012challenge的回顾.  

### Abstract  
PASCAL VOC(pattern analysis,statistical modelling and computational learning    visual object classes)主要包含两个主要部分：（1）一个公开可用的数据集，包含ground truth annotaion和标准化的评估软件；（2）每年一届的比赛和研讨会.  
为了评估在VOC数据集上提交的算法，我们引入了许多novel的方法：（1）一种用于确定两种算法的性能差异是否显著的自举方法（2）归一化的平均精度(AP)，使得性能可以在具有不同比例的正实例的类中进行比较（3）一种用于在多个算法上可视化性能的聚类方法，以便可以识别硬而简单的图像（4）对所提交的算法使用联合分类器，以便测量它们的互补性和组合性能.

### 文章主体  
这篇文章是一篇比较长的文章，所以我也没有全部详细阅读本文，只是主要关注了Submission and Evaluation部分.  
Section 2是对VOC challenge的回顾.关于voc2012竞赛、数据集、标注步骤和评估标准做了一个简单的介绍.  
Section 3对voc2012的各项结果进行了展示，然后使用新颖的方法对2012比赛结果进行了分析，最后提出了一种方法对在同样的testset上进行预测的方法进行公平的比较，摘要中的方法（1）.  
Section 4进行评估，并尝试回答关于我们的领域在可能或不能解决的分类和检测问题方面的更广泛的问题，摘要中提出的（2）（3）方法用于此处.  
Section 5调查不同方法的互补性水平.摘要中的（4）方法(super methods).  
Section 6考虑在时间上的进步.  

### Submission and evaluation  
竞赛的过程包括两个阶段：第一个阶段，每个参赛者会被分发一个开发者套件：包括train/val图片和标注信息，以及使用matlab软件可以访问的标注文件(xml文件).第二阶段是在test上进行提交.test数据大概在提交结果的前三个才发布.  
**Detection任务的评估**  
![test](https://raw.githubusercontent.com/su526664687/PictureLibrary/master/Paper/PascalVoC1.png)  
这里引入了另一个指标IoU，定义Bp是预测的区域，Bgt是ground true，两者的交面积除以两者的并的面积(intersection over Union)，就是IoU值.这个值大于50%才认为方法有效.PASCALVOC给出的评测结果就是在IoU>=0.5的情况下的mAP值.  
**Segmentation任务的评估**  
![test](https://raw.githubusercontent.com/su526664687/PictureLibrary/master/Paper/PascalVoC2.png)
对每个类都采用IoU.   
**mAP**  
采用了每个类别的P-R图的面积作为该类别mAP值.在2007年之前使用的ROC-AUC.关于mAP的具体介绍可以参考我的另一篇文章.
