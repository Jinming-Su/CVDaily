# 安装gpu驱动
1. 先查看gpu是否是英伟达的  
`lspci | grep -i nvidia`  
![1](http://i1.buimg.com/589172/92e9a3592b166265.png)  
2. 查看系统架构
`uname -m && cat /etc/*release ` // x86_64才能安装caffe
3. 安装nvidia驱动`(如果没安装的话)
下载地址: `http://www.geforce.cn/drivers`  
安装:  
```
sudo chmod +x NVIDIA**.run
关闭X-Window，很简单：sudo service lightdm stop，然后切换到tty1：Ctrl+Alt+F1即可
sudo ./NVIDIA.run开始安装，安装过程比较快，根据提示选择即可
安装完毕后，重新启动X-Window：sudo service lightdm start，然后Ctrl+Alt+F7进入图形界面
查看显卡驱动安装情况nvidia-smi
```

# 安装cuda
1. 查看gpu是否支持cuda(Compute Unified Device Architecture)，以及计算容量  
浏览网页查看`https://developer.nvidia.com/cuda-gpus`  
2. 如果本机gpu支持cuda，就可以安装cuda了
下载地址: `https://developer.nvidia.com/cuda-downloads`  
![1](http://i1.buimg.com/589172/29439ec3d4e5ad28.png)  

# 安装cudnn
1. 安装cuDNN(NVIDIA cuDNN是用于深度神经网络的GPU加速库)
下载地址: `https://developer.nvidia.com/rdp/cudnn-download`(需要注册)
安装:  

```
// 拷贝cuDNN库文件到cuda目录下
tar -zxvf cudnn-7.0-linux-x64-v4.0-prod.tgz
cd cuda
sudo cp lib64/* /usr/local/cuda/lib64/
sudo cp include/cudnn.h /usr/local/cuda/include/

//设置环境变量，在/etc/profile中添加CUDA环境变量
sudo gedit /etc/profile
//添加
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

//进入/usr/local/cuda/samples，执行下面的命令来build samples
sudo make all -j4
//全部编译完成后，进入 samples/bin/x86_64/linux/release，运行deviceQuery
./deviceQuery

//如果出现显卡信息，则驱动及显卡安装成功
```
