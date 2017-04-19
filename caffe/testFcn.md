
```
clear
clc

addpath ../../matlab
caffe.set_mode_cpu();
% init_net
deploy = 'voc-fcn8s/deploy.prototxt';
caffe_model = 'voc-fcn8s/fcn8s-heavy-pascal.caffemodel';
net = caffe.Net(deploy, caffe_model, 'test');

im_data = imread('voc-fcn8s/test.png');
im_data = single(im_data); 
im_data = imresize(im_data, [500 500]);
im_data = im_data(:, :, [3, 2, 1]); % matlab按照RGB读取图片，opencv是BGR，所以需要转换顺序为opencv处理格式  
im_data = permute(im_data, [2, 1, 3]); % flip width and height, blob 通常的 4 个维度在 Matlab中用[width, height, channels, num]表示
mean_data(:,:,1) = 104.00698793 * ones(500, 500); 
mean_data(:,:,2) = 116.66876762 * ones(500, 500);
mean_data(:,:,3) = 122.67891434 * ones(500, 500);
im_data = im_data - mean_data;

net.blobs('data').reshape([500 500 3 1]);
net.blobs('data').set_data(im_data);
net.forward_prefilled();

[out I] = max(net.blobs('score').get_data(),[],3);
imshow(permute(out, [2, 1, 3])/256);
```
