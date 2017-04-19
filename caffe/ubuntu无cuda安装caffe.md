###说明
* cuda即compute unified device architecture.是NVIDIA推出的运算平台，所以amd不支持，不错据说2015年后开始，amd可能支持cuda.

### 外部依赖库安装
* caffe有很多外部依赖库，这些库可以通过apt-get管理器进行安装
* 安装opencv(一个开源计算机视觉库)
    `sudo apt-get install libopencv-dev`
* 安装bootst(它是一个可移植、跨平台，提供源代码的C++库，作为标准库的后备)及依赖
    
    ```
    sudo apt-get install libboost-all-dev
    sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev  
    sudo apt-get install libhdf5-serial-dev protobuf-compiler 
    ```
* 安装blas(基础线性代数子程序库，里面拥有大量已经编写好的关于线性代数运算的程序)及依赖
    
    ```
    sudo apt-get install libatlas-base-dev 
    sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev 
    ```

### 安装caffe
* 下载caffe
    `git clone git://github.com/BVLC/caffe.git`
* 在该目录下拷贝makefile配置文件
    `cp Makefile.config.example Makefile.config `
* 由于没有cuda，修改makefile.config文件CPU_ONLY:= 1 前面的“#”去掉
* 编译
    
    ```
    make all
    make test
    make runtest
    ```
### 测试例程mnist
* 运行脚本程序获取MNIST数据集，并将其转换为lmdb格式
    
    ```
    ./data/mnist/get_mnist.sh
    ./examples/mnist/create_mnist.sh
    ```
* `因为不用GPU ，所以在训练前，要将caffe/examples/mnist/lenet_solver.prototxt中的solver_mode设置成solver_mode: CPU`
* 训练网络
    `./examples/mnist/train_lenet.sh`
