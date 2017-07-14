#!/usr/bin/python
#encoding: utf-8

import tensorflow as tf
import numpy as np

filename = '/home/hcxy/Desktop/test1.csv'
col_num = 6
row_num = 9

def read_csv():
    filename_queue = tf.train.string_input_producer([filename])
    reader = tf.TextLineReader()
    key, value = reader.read(filename_queue)
    
    record_defaults = [[]]*(col_num)
    col = tf.decode_csv(value, record_defaults = record_defaults)
    feature = tf.stack(col[0:col_num - 1])
    
    with tf.Session() as sess:
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)
        
        example, label = sess.run([feature, col[col_num - 1]])
        examples = np.array([example])
        labels = np.array([label])
        for _ in range(1,row_num):
            example, label = sess.run([feature, col[col_num - 1]])
            examples = np.row_stack((examples, example))
            labels = np.row_stack((labels, label))
        return examples, labels
        coord.request_stop()
        coord.join(threads)

def add_layer(inputs, in_size, out_size, activation_function=None):
    W = tf.Variable(tf.random_normal([in_size, out_size]))
    b = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    xW_plus_b = tf.matmul(inputs, W,) + b
    if activation_function is None:
        outputs = xW_plus_b
    else:
        outputs = activation_function(xW_plus_b)
    return outputs

def net():
    # define placeholder
    x = tf.placeholder(tf.float32, [None, col_num - 1])
    y = tf.placeholder(tf.float32, [None, 1])
    
    
    
    
    

    
