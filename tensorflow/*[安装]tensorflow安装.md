# 安装
先安装好cuda和cudnn，然后再安装tensorflow  
<br/>
tensorflow的安装十分简单，一般采用apt的方法进行安装，命令如下:  
```
# 仅使用 CPU 的版本
$ pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.5.0-cp27-none-linux_x86_64.whl

# 开启 GPU 支持的版本 (安装该版本的前提是已经安装了 CUDA sdk)
$ pip install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.5.0-cp27-none-linux_x86_64.whl
```
上述是官方提供的方法，但是tensorflow的不同版本对本机gpu环境(cuda和cudnn版本)有不同的要求的，我的配置是cuda8.0和cudnn5.1，使用的tensorflow是1.0.1版本的，命令如下:  
`sudo pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.0.1-cp27-none-linux_x86_64.whl`

# 相关资源
* 中文文档 http://www.tensorfly.cn/tfdoc/tutorials/overview.html
