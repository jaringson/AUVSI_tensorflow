#!/usr/bin/env python
import tensorflow as tf
import shape_letter_image as sli
import numpy as np
sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32, shape=[None, 24*24*3])
let_ = tf.placeholder(tf.float32, shape=[None, 36])
sha_ = tf.placeholder(tf.float32, shape=[None, 8])
let_col_ = tf.placeholder(tf.float32, shape=[None, 8])
sha_col_ = tf.placeholder(tf.float32, shape=[None, 8])


def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.2)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

with tf.name_scope('layers') as scope:
    W_conv1 = weight_variable([5, 5, 3, 32])
    b_conv1 = bias_variable([32])
    x_image = tf.reshape(x, [-1,24,24,3])
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    W_fc1 = weight_variable([6 * 6 * 64, 1024])
    b_fc1 = bias_variable([1024])
    h_pool2_flat = tf.reshape(h_pool2, [-1, 6 * 6 * 64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    with tf.variable_scope("letter"):
        W_fc2 = tf.get_variable( "W", [1024, 36], tf.float32,
                                  tf.random_normal_initializer( stddev=np.sqrt(2 / np.prod(h_fc1_drop.get_shape().as_list()[1:])) ) ) # weight_variable([1024, 36])
        b_fc2 = bias_variable([36])
        let_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

    with tf.variable_scope("shape"):
        W_fc2 = tf.get_variable( "W", [1024, 8], tf.float32,
                                  tf.random_normal_initializer( stddev=np.sqrt(2 / np.prod(h_fc1_drop.get_shape().as_list()[1:])) ) ) # weight_variable([1024, 36])
        b_fc2 = bias_variable([8])
        sha_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

    with tf.variable_scope("letter_color"):
        W_fc2 = tf.get_variable( "W", [1024, 8], tf.float32,
                                  tf.random_normal_initializer( stddev=np.sqrt(2 / np.prod(h_fc1_drop.get_shape().as_list()[1:])) ) ) # weight_variable([1024, 36])
        b_fc2 = bias_variable([8])
        let_col_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

    with tf.variable_scope("shape_color"):
        W_fc2 = tf.get_variable( "W", [1024, 8], tf.float32,
                                  tf.random_normal_initializer( stddev=np.sqrt(2 / np.prod(h_fc1_drop.get_shape().as_list()[1:])) ) ) # weight_variable([1024, 36])
        b_fc2 = bias_variable([8])
        sha_col_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

with tf.name_scope('Cost') as scope:
    cross_entropies = tf.reduce_mean(-tf.reduce_sum(let_ * tf.log(let_conv), reduction_indices=[1])) + \
                      tf.reduce_mean(-tf.reduce_sum(sha_ * tf.log(sha_conv), reduction_indices=[1])) + \
                      tf.reduce_mean(-tf.reduce_sum(let_col_ * tf.log(let_col_conv), reduction_indices=[1])) + \
                      tf.reduce_mean(-tf.reduce_sum(sha_col_ * tf.log(sha_col_conv), reduction_indices=[1]))
with tf.name_scope('Optimizer') as scope:
    train_step = tf.train.AdamOptimizer(1e-8).minimize(cross_entropies)
with tf.name_scope('Accuracy') as scope:
    let_correct_prediction = tf.equal(tf.argmax(let_conv,1), tf.argmax(let_,1))
    let_acc = tf.reduce_mean(tf.cast(let_correct_prediction, tf.float32))
    sha_correct_prediction = tf.equal(tf.argmax(sha_conv,1), tf.argmax(sha_,1))
    sha_acc = tf.reduce_mean(tf.cast(sha_correct_prediction, tf.float32))
    let_col_correct_prediction = tf.equal(tf.argmax(let_col_conv,1), tf.argmax(let_col_,1))
    let_col_acc = tf.reduce_mean(tf.cast(let_col_correct_prediction, tf.float32))
    sha_col_correct_prediction = tf.equal(tf.argmax(sha_col_conv,1), tf.argmax(sha_col_,1))
    sha_col_acc = tf.reduce_mean(tf.cast(sha_col_correct_prediction, tf.float32))

acc_summary = tf.scalar_summary( 'letter accuracy', let_acc )
acc_summary = tf.scalar_summary( 'shape accuracy', sha_acc )
cost_summary = tf.scalar_summary( 'cost', cross_entropies )

merged_summary_op = tf.merge_all_summaries()
summary_writer = tf.train.SummaryWriter("./tf_logs",graph=sess.graph)
sess.run(tf.initialize_all_variables())
print("step, shape_color, letter_color, shape, letter")
for i in range(1500):
  #batch = mnist.train.next_batch(50)
  batch = sli.next_target_batch(150)
  # print len(batch[0][0])
  # print len(batch[1][0])
  # print batch[0][0][0:30]
  if i%10 == 0:
    l,s,lc,sc = sess.run([let_acc, sha_acc,let_col_acc,sha_col_acc],feed_dict={x:batch[0], let_: batch[1], sha_: batch[2], let_col_: batch[3], sha_col_: batch[4], keep_prob: 1.0})
    if i%100 == 0:
        # print("%d, %g"%(i, sc,lc,s,l))
        print("%d, %g, %g, %g, %g"%(i, sc,lc,s,l))
    summary_str, = sess.run([merged_summary_op],feed_dict={x: batch[0], let_: batch[1], sha_: batch[2], let_col_: batch[3], sha_col_: batch[4], keep_prob: 0.5})
    summary_writer.add_summary(summary_str,i)
  train_step.run(feed_dict={x: batch[0], let_: batch[1], sha_: batch[2], let_col_: batch[3], sha_col_: batch[4], keep_prob: 0.5})
