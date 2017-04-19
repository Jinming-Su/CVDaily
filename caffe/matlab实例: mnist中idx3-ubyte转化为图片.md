## mnist中idx3-ubyte转化为图片
* 在网上找了一个代码，测试了一下，可以转化出10000张图片
    
    ```
    % Matlab_Read_t10k-images_idx3.m
    % 用于读取MNIST数据集中t10k-images.idx3-ubyte文件并将其转换成bmp格式图片输出。
    % 用法：运行程序，会弹出选择测试图片数据文件t10k-labels.idx1-ubyte路径的对话框和
    % 选择保存测试图片路径的对话框，选择路径后程序自动运行完毕，期间进度条会显示处理进度。
    % 图片以TestImage_00001.bmp～TestImage_10000.bmp的格式保存在指定路径，10000个文件占用空间39M。。
    % 整个程序运行过程需几分钟时间。
     
    clear all;
    clc;
    %读取训练图片数据文件
    [FileName,PathName] = uigetfile('*.*','选择测试图片数据文件t10k-images.idx3-ubyte');
    TrainFile = fullfile(PathName,FileName);
    fid = fopen(TrainFile,'r'); %fopen（）是最核心的函数，导入文件，‘r’代表读入
    a = fread(fid,16,'uint8'); %这里需要说明的是，包的前十六位是说明信息，从上面提到的那个网页可以看到具体那一位代表什么意义。所以a变量提取出这些信息，并记录下来，方便后面的建立矩阵等动作。
    MagicNum = ((a(1)*256+a(2))*256+a(3))*256+a(4);  %进制转化
    ImageNum = ((a(5)*256+a(6))*256+a(7))*256+a(8);
    ImageRow = ((a(9)*256+a(10))*256+a(11))*256+a(12);
    ImageCol = ((a(13)*256+a(14))*256+a(15))*256+a(16);
    %从上面提到的网页可以理解这四句
    if ((MagicNum~=2051)||(ImageNum~=10000))
        error('不是 MNIST t10k-images.idx3-ubyte 文件！');
        fclose(fid);   
        return;   
    end %排除选择错误的文件。
    savedirectory = uigetdir('','选择测试图片路径：');
    h_w = waitbar(0,'请稍候，处理中>>');
    for i=1:ImageNum
        b = fread(fid,ImageRow*ImageCol,'uint8');   %fread（）也是核心的函数之一，b记录下了一副图的数据串。注意这里还是个串，是看不出任何端倪的。
        c = reshape(b,[ImageRow ImageCol]); %亮点来了，reshape重新构成矩阵，终于把串转化过来了。众所周知图片就是矩阵，这里reshape出来的灰度矩阵就是该手写数字的矩阵了。
        d = c'; %转置一下，因为c的数字是横着的。。。
        e = 255-d; %根据灰度理论，0是黑色，255是白色，为了弄成白底黑字就加入了e
        e = uint8(e);
        savepath = fullfile(savedirectory,['TestImage_' num2str(i,d) '.bmp']);
        imwrite(e,savepath,'bmp'); %最后用imwrite写出图片
        waitbar(i/ImageNum);
    end
    fclose(fid);
    close(h_w);
    ```

### matlab函数学习
* uigetfile.显示一个模态对话框,对话框列出了当前目录下的文件和目录,用于可以选择一个将要打开的文件名。
    
    ```
    [FileName,PathName,FilterIndex] = uigetfile(FilterSpec,DialogTitle,DefaultName)
    //举例
    [FileName,PathName] = uigetfile('*.m','Select the M-file');
    ```
* fullfile.利用文件各部分信息创建并合成完整文件名
    
    ```
    f = fullfile(PathName,FileName)
    ```
* imwrite.将图像数据写入到图像文件中， 存储在磁盘上.

    ```
    imwrite(ImageDate,filename,fmt)
    ```

### 修改后，生成一张由100x100张小图片组成的大图片
* 修改后的代码
    
    ```
    clear all;
    clc;
    %读取训练图片数据文件
    [FileName,PathName] = uigetfile('*.*','选择测试图片数据文件t10k-images.idx3-ubyte');
    TrainFile = fullfile(PathName,FileName);
    fid = fopen(TrainFile,'r'); %fopen（）是最核心的函数，导入文件，‘r’代表读入
    a = fread(fid,16,'uint8'); %这里需要说明的是，包的前十六位是说明信息，从上面提到的那个网页可以看到具体那一位代表什么意义。所以a变量提取出这些信息，并记录下来，方便后面的建立矩阵等动作。
    MagicNum = ((a(1)*256+a(2))*256+a(3))*256+a(4);  %进制转化
    ImageNum = ((a(5)*256+a(6))*256+a(7))*256+a(8);
    ImageRow = ((a(9)*256+a(10))*256+a(11))*256+a(12);
    ImageCol = ((a(13)*256+a(14))*256+a(15))*256+a(16);
    %从上面提到的网页可以理解这四句
    if ((MagicNum~=2051)||(ImageNum~=10000))
        error('不是 MNIST t10k-images.idx3-ubyte 文件！');
        fclose(fid);   
        return;   
    end %排除选择错误的文件。
    savedirectory = uigetdir('','选择测试图片路径：');
    h_w = waitbar(0,'请稍候，处理中>>');
    myAns = [];
    myRow = [];
    for i=1: 100
        for j=1: 100
            b = fread(fid,ImageRow*ImageCol,'uint8');   %fread（）也是核心的函数之一，b记录下了一副图的数据串。注意这里还是个串，是看不出任何端倪的。
            c = reshape(b,[ImageRow ImageCol]); %亮点来了，reshape重新构成矩阵，终于把串转化过来了。众所周知图片就是矩阵，这里reshape出来的灰度矩阵就是该手写数字的矩阵了。
            d = c'; %转置一下，因为c的数字是横着的。。。
            e = 255-d; %根据灰度理论，0是黑色，255是白色，为了弄成白底黑字就加入了e
            e = uint8(e);
            myRow = [myRow e];
            waitbar(i/ImageNum);
        end
        myAns = [myAns;myRow];
        myRow=[];
    end
    savepath = fullfile(savedirectory,['TestImage.bmp']);
    imwrite(myAns,savepath,'bmp'); %最后用imwrite写出图片
    fclose(fid);
    close(h_w);
    ```
* 结果截图
    
![1](https://cloud.githubusercontent.com/assets/16068384/22775842/586e0d12-eee8-11e6-92eb-8f9a124b459d.png)
