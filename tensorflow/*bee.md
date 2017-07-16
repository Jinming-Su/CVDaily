# 数据
```
1	1	2	1	1	1
1	1	3	2	2	2
1	1	4	3	3	3
1	1	5	4	4	4
1	2	1	1	1	1
1	2	2	2	2	2
1	2	3	3	3	3
1	2	4	4	4	4
2	1	1	1	1	1
2	1	2	2	2	2
2	1	3	3	3	3
2	1	4	4	4	4
1	1	2	1	1	1
1	1	3	2	2	2
1	1	4	3	3	3
1	1	5	4	4	4
1	2	1	1	1	1
1	2	2	2	2	2
1	2	3	3	3	3
1	2	4	4	4	4
2	1	1	1	1	1
2	1	2	2	2	2
2	1	3	3	3	3
2	1	4	4	4	4
```

# 训练
```
#!/usr/bin/python
#encoding: utf-8

import tensorflow as tf
import numpy as np

filename = '/home/sujinming/Desktop/test.csv' 
col_num = 6   # 数据的列数
row_num = 24   # 数据的行数
class_num = 5    # 数据的类别数+1
train_test_rate = 6    # 训练集与测试集比例

def read_csv():
    filename_queue = tf.train.string_input_producer([filename])
    reader = tf.TextLineReader()
    key, value = reader.read(filename_queue)
    
    record_defaults = [[]]*(col_num)
    col = tf.decode_csv(value, record_defaults = record_defaults)
    data = tf.stack(col[0:col_num])
    
    with tf.Session() as sess:
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)
        
        example = sess.run(data)
        examples = np.array([example])
        for _ in range(1,row_num):
            example = sess.run([data])
            examples = np.row_stack((examples, example))
        return examples
        coord.request_stop()
        coord.join(threads)

def weight_variable(shape):
    init = tf.random_normal(shape)
    return tf.Variable(init)

def bias_variable(shape):
    init = tf.constant(0.1, shape=shape)
    return tf.Variable(init)
    
def net(train_data, train_label, test_data, test_label):
    # define placeholder
    x = tf.placeholder(tf.float32, [None, col_num - 1])
    yt = tf.placeholder(tf.float32, [None, class_num])

    W_fc1 = weight_variable([col_num - 1, 16])
    b_fc1 = bias_variable([16])
    y_fc1 = tf.nn.relu(tf.matmul(x, W_fc1) + b_fc1)
    
#     W_fc2 = weight_variable([4, 8])
#     b_fc2 = bias_variable([8])
#     y_fc2 = tf.nn.relu(tf.matmul(y_fc1, W_fc2) + b_fc2)
#      
#     W_fc3 = weight_variable([8, 16])
#     b_fc3 = bias_variable([16])
#     y_fc3 = tf.nn.relu(tf.matmul(y_fc2, W_fc3) + b_fc3)
#      
#     W_fc4 = weight_variable([16, 32])
#     b_fc4 = bias_variable([32])
#     y_fc4 = tf.nn.relu(tf.matmul(y_fc3, W_fc4) + b_fc4)
#     
    W_fc5 = weight_variable([16, class_num])
    b_fc5 = bias_variable([class_num])
    y = tf.nn.softmax(tf.matmul(y_fc1, W_fc5) + b_fc5)
    
    cross_entropy = -tf.reduce_sum(yt * tf.log(y))
#     cross_entropy = tf.reduce_mean(tf.reduce_sum(tf.square(yt - y),
#                      reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
    
    # 对矩阵按行或列计算最大值, 0表示按列，1表示按行
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(yt, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    
    for i in range(5000):
        sess.run(train_step, feed_dict={x: train_data, yt: train_label})
        # print sess.run(correct_prediction, feed_dict={x: train_data, yt: train_label})
        if i%200 == 0:
            print "test accuracy: " , sess.run(accuracy, feed_dict={x: test_data, yt: test_label})
    saver = tf.train.Saver()
    save_path = saver.save(sess, "save_net.bak")
    sess.close()
    
examples = read_csv()

np.random.shuffle(examples)
data = examples
label = data[:,col_num - 1][:, np.newaxis]
data = data[:, 0 : col_num - 1]

label = (np.arange(class_num) == label[:]).astype(np.float32)
train_data = data[0: row_num * train_test_rate / (train_test_rate + 1)]
train_label = label[0: row_num * train_test_rate / (train_test_rate + 1)]
test_data = data[row_num * train_test_rate / (train_test_rate + 1) + 1 : row_num]
test_label = label[row_num * train_test_rate / (train_test_rate + 1) + 1 : row_num]
net(train_data, train_label, test_data, test_label)
```
# 测试
```
#!/usr/bin/python
#encoding: utf-8

import tensorflow as tf
import numpy as np

col_num = 6  
class_num = 5

def weight_variable(shape):
    init = tf.random_normal(shape)
    return tf.Variable(init)

def bias_variable(shape):
    init = tf.constant(0.1, shape=shape)
    return tf.Variable(init)
    
def test():
    # define placeholder
    x = tf.placeholder(tf.float32, [None, col_num - 1])

    W_fc1 = weight_variable([col_num - 1, 16])
    b_fc1 = bias_variable([16])
    y_fc1 = tf.nn.relu(tf.matmul(x, W_fc1) + b_fc1)
    
#     W_fc2 = weight_variable([4, 8])
#     b_fc2 = bias_variable([8])
#     y_fc2 = tf.nn.relu(tf.matmul(y_fc1, W_fc2) + b_fc2)
#      
#     W_fc3 = weight_variable([8, 16])
#     b_fc3 = bias_variable([16])
#     y_fc3 = tf.nn.relu(tf.matmul(y_fc2, W_fc3) + b_fc3)
#      
#     W_fc4 = weight_variable([16, 32])
#     b_fc4 = bias_variable([32])
#     y_fc4 = tf.nn.relu(tf.matmul(y_fc3, W_fc4) + b_fc4)
#     
    W_fc5 = weight_variable([16, class_num])
    b_fc5 = bias_variable([class_num])
    y = tf.nn.softmax(tf.matmul(y_fc1, W_fc5) + b_fc5)
    
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    save_path = saver.restore(sess, "save_net.bak")
    
    print sess.run(y, feed_dict={x: np.array([1,1,2,1,1])[np.newaxis, :]})
    
    sess.close()

test()
```
