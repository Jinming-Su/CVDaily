#!/usr/bin/python
# -*- coding: utf-8 -*-  

import input_data  
import tensorflow as tf  
  
# MNIST数据输入  
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)  

# tf.placeholder(dtype, shape, name)
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# tf.nn.softmax(logits, dim, name)
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])

# y_ * tf.log(y)属于numpy中的数组，单个元素运算
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
# 学习率0.01
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

# tf.argmax(input, axis=None, name=None, dimension=None)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# tf.cast(x, dtype, name=None) 将x或者x.values转换为dtype
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

for i in range(10000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    if i % 1000 == 0:
        print sess.run(accuracy, feed_dict = {x: mnist.test.images, y_ : mnist.test.labels})
