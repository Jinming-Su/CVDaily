# train.prototxt
```
name: "VGG_ILSVRC_16_layer"
layer {
  name: "data"
  type: "Data"
  top: "data"
  top: "label"
  include {
    phase: TRAIN
  }
  transform_param {
    mirror: true
    crop_size: 224
    mean_file: "data/data.binaryproto"
  }
  data_param {
    source: "data/train_lmdb"
    batch_size: 2
    backend: LMDB
  }
}
layer {
  name: "data"
  type: "Data"
  top: "data"
  top: "label"
  include {
    phase: TEST
  }
  transform_param {
    mirror: false
    crop_size: 224
    mean_file: "data/data.binaryproto"
  }
  data_param {
    source: "data/test_lmdb"
    batch_size: 2
    backend: LMDB
  }
}
layer {
  bottom: "data"
  top: "conv1_1"
  name: "conv1_1"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 64
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv1_1"
  top: "conv1_1"
  name: "relu1_1"
  type: "ReLU"
}
layer {
  bottom: "conv1_1"
  top: "conv1_2"
  name: "conv1_2"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 64
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv1_2"
  top: "conv1_2"
  name: "relu1_2"
  type: "ReLU"
}
layer {
  bottom: "conv1_2"
  top: "pool1"
  name: "pool1"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool1"
  top: "conv2_1"
  name: "conv2_1"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 128
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv2_1"
  top: "conv2_1"
  name: "relu2_1"
  type: "ReLU"
}
layer {
  bottom: "conv2_1"
  top: "conv2_2"
  name: "conv2_2"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 128
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv2_2"
  top: "conv2_2"
  name: "relu2_2"
  type: "ReLU"
}
layer {
  bottom: "conv2_2"
  top: "pool2"
  name: "pool2"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool2"
  top: "conv3_1"
  name: "conv3_1"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 256
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv3_1"
  top: "conv3_1"
  name: "relu3_1"
  type: "ReLU"
}
layer {
  bottom: "conv3_1"
  top: "conv3_2"
  name: "conv3_2"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 256
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv3_2"
  top: "conv3_2"
  name: "relu3_2"
  type: "ReLU"
}
layer {
  bottom: "conv3_2"
  top: "conv3_3"
  name: "conv3_3"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 256
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv3_3"
  top: "conv3_3"
  name: "relu3_3"
  type: "ReLU"
}
layer {
  bottom: "conv3_3"
  top: "pool3"
  name: "pool3"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool3"
  top: "conv4_1"
  name: "conv4_1"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv4_1"
  top: "conv4_1"
  name: "relu4_1"
  type: "ReLU"
}
layer {
  bottom: "conv4_1"
  top: "conv4_2"
  name: "conv4_2"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv4_2"
  top: "conv4_2"
  name: "relu4_2"
  type: "ReLU"
}
layer {
  bottom: "conv4_2"
  top: "conv4_3"
  name: "conv4_3"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv4_3"
  top: "conv4_3"
  name: "relu4_3"
  type: "ReLU"
}
layer {
  bottom: "conv4_3"
  top: "pool4"
  name: "pool4"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool4"
  top: "conv5_1"
  name: "conv5_1"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv5_1"
  top: "conv5_1"
  name: "relu5_1"
  type: "ReLU"
}
layer {
  bottom: "conv5_1"
  top: "conv5_2"
  name: "conv5_2"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv5_2"
  top: "conv5_2"
  name: "relu5_2"
  type: "ReLU"
}
layer {
  bottom: "conv5_2"
  top: "conv5_3"
  name: "conv5_3"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv5_3"
  top: "conv5_3"
  name: "relu5_3"
  type: "ReLU"
}
layer {
  bottom: "conv5_3"
  top: "pool5"
  name: "pool5"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool5"
  top: "fc6"
  name: "fc6"
  type: "InnerProduct"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  inner_product_param {
    num_output: 4096
    weight_filler {
      type: "gaussian"
      std: 0.005
    }
    bias_filler {
      type: "constant"
      value: 0.1
    }
  }
}
layer {
  bottom: "fc6"
  top: "fc6"
  name: "relu6"
  type: "ReLU"
}
layer {
  bottom: "fc6"
  top: "fc6"
  name: "drop6"
  type: "Dropout"
  dropout_param {
    dropout_ratio: 0.5
  }
}
layer {
  bottom: "fc6"
  top: "fc7"
  name: "fc7"
  type: "InnerProduct"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  inner_product_param {
    num_output: 4096
    weight_filler {
      type: "gaussian"
      std: 0.005
    }
    bias_filler {
      type: "constant"
      value: 0.1
    }
  }
}
layer {
  bottom: "fc7"
  top: "fc7"
  name: "relu7"
  type: "ReLU"
}
layer {
  bottom: "fc7"
  top: "fc7"
  name: "drop7"
  type: "Dropout"
  dropout_param {
    dropout_ratio: 0.5
  }
}
layer {
  name: "fc8_new"
  bottom: "fc7"
  top: "fc8_new"
  type: "InnerProduct"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  inner_product_param {
    num_output: 3
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  name: "accuracy"
  type: "Accuracy"
  bottom: "fc8_new"
  bottom: "label"
  top: "accuracy"
  include {
    phase: TEST
  }
}
layer{
  name: "loss"
  type: "SoftmaxWithLoss"
  bottom: "fc8_new"
  bottom: "label"
  top: "loss"
}
```
# inference.prototxt
这个可以自行修改一下就可以得到了，简单贴一下  
```
layer {
  name: "data"
  type: "Input"
  top: "data"
  input_param { shape: { dim: 1 dim: 3 dim: 224 dim: 224} }
}
layer {
  bottom: "data"
  top: "conv1_1"
  name: "conv1_1"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 64
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv1_1"
  top: "conv1_1"
  name: "relu1_1"
  type: "ReLU"
}
layer {
  bottom: "conv1_1"
  top: "conv1_2"
  name: "conv1_2"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 64
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv1_2"
  top: "conv1_2"
  name: "relu1_2"
  type: "ReLU"
}
layer {
  bottom: "conv1_2"
  top: "pool1"
  name: "pool1"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool1"
  top: "conv2_1"
  name: "conv2_1"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 128
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv2_1"
  top: "conv2_1"
  name: "relu2_1"
  type: "ReLU"
}
layer {
  bottom: "conv2_1"
  top: "conv2_2"
  name: "conv2_2"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 128
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv2_2"
  top: "conv2_2"
  name: "relu2_2"
  type: "ReLU"
}
layer {
  bottom: "conv2_2"
  top: "pool2"
  name: "pool2"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool2"
  top: "conv3_1"
  name: "conv3_1"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 256
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv3_1"
  top: "conv3_1"
  name: "relu3_1"
  type: "ReLU"
}
layer {
  bottom: "conv3_1"
  top: "conv3_2"
  name: "conv3_2"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 256
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv3_2"
  top: "conv3_2"
  name: "relu3_2"
  type: "ReLU"
}
layer {
  bottom: "conv3_2"
  top: "conv3_3"
  name: "conv3_3"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 256
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv3_3"
  top: "conv3_3"
  name: "relu3_3"
  type: "ReLU"
}
layer {
  bottom: "conv3_3"
  top: "pool3"
  name: "pool3"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool3"
  top: "conv4_1"
  name: "conv4_1"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv4_1"
  top: "conv4_1"
  name: "relu4_1"
  type: "ReLU"
}
layer {
  bottom: "conv4_1"
  top: "conv4_2"
  name: "conv4_2"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv4_2"
  top: "conv4_2"
  name: "relu4_2"
  type: "ReLU"
}
layer {
  bottom: "conv4_2"
  top: "conv4_3"
  name: "conv4_3"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv4_3"
  top: "conv4_3"
  name: "relu4_3"
  type: "ReLU"
}
layer {
  bottom: "conv4_3"
  top: "pool4"
  name: "pool4"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool4"
  top: "conv5_1"
  name: "conv5_1"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv5_1"
  top: "conv5_1"
  name: "relu5_1"
  type: "ReLU"
}
layer {
  bottom: "conv5_1"
  top: "conv5_2"
  name: "conv5_2"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv5_2"
  top: "conv5_2"
  name: "relu5_2"
  type: "ReLU"
}
layer {
  bottom: "conv5_2"
  top: "conv5_3"
  name: "conv5_3"
  type: "Convolution"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    kernel_size: 3
    pad: 1
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "conv5_3"
  top: "conv5_3"
  name: "relu5_3"
  type: "ReLU"
}
layer {
  bottom: "conv5_3"
  top: "pool5"
  name: "pool5"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool5"
  top: "fc6"
  name: "fc6"
  type: "InnerProduct"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  inner_product_param {
    num_output: 4096
    weight_filler {
      type: "gaussian"
      std: 0.005
    }
    bias_filler {
      type: "constant"
      value: 0.1
    }
  }
}
layer {
  bottom: "fc6"
  top: "fc6"
  name: "relu6"
  type: "ReLU"
}
layer {
  bottom: "fc6"
  top: "fc6"
  name: "drop6"
  type: "Dropout"
  dropout_param {
    dropout_ratio: 0.5
  }
}
layer {
  bottom: "fc6"
  top: "fc7"
  name: "fc7"
  type: "InnerProduct"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  inner_product_param {
    num_output: 4096
    weight_filler {
      type: "gaussian"
      std: 0.005
    }
    bias_filler {
      type: "constant"
      value: 0.1
    }
  }
}
layer {
  bottom: "fc7"
  top: "fc7"
  name: "relu7"
  type: "ReLU"
}
layer {
  bottom: "fc7"
  top: "fc7"
  name: "drop7"
  type: "Dropout"
  dropout_param {
    dropout_ratio: 0.5
  }
}
layer {
  name: "fc8_new"
  bottom: "fc7"
  top: "fc8_new"
  type: "InnerProduct"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  inner_product_param {
    num_output: 3
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  name: "prob"
  type: "Softmax"
  bottom: "fc8_new"
  top: "prob"
}
```

# VGG_ILSVRC_16_layers.caffemodel
这个文件一般比较难找，上传到百度网盘了，自行下载吧  
链接: https://pan.baidu.com/s/1o8FkDqa 密码: fpek
