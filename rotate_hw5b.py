#!/usr/bin/env python
import tensorflow as tf
from scipy.misc import imsave
import batch_utils
import numpy as np
import vgg16
from spatial_transformer import transformer
sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32, shape=[None, 224*224*3])
y_ = tf.placeholder(tf.float32)
keep_prob = tf.placeholder(tf.float32)

def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

x_image = tf.reshape(x, [-1,224,224,3])
trans = tf.concat([0.09*tf.ones_like(y_), tf.zeros_like(y_), tf.zeros_like(y_), tf.zeros_like(y_), 0.09*tf.ones_like(y_), tf.zeros_like(y_)], 1)
print trans.shape
x_trans = transformer(x_image, trans, (32,32))

with tf.variable_scope('rotator_network') as rotate_scope:
    W_conv1 = weight_variable([5, 5, 3, 32])
    b_conv1 = bias_variable([32])
    h_conv1 = tf.nn.relu(conv2d(x_trans, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    W_conv2 = weight_variable([5, 5, 32, 32])
    b_conv2 = bias_variable([32])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    W_fc1 = weight_variable([8*8*32, 1024])
    b_fc1 = bias_variable([1024])
    h_pool2_flat = tf.reshape(h_pool2, [-1, 8*8*32])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    initial = np.array([0])
    initial = initial.astype('float32')
    initial = initial.flatten()

    W_fc2 = tf.Variable(tf.truncated_normal([1024,1], stddev=1e-8))# tf.zeros([1024, 3]) # weight_variable([1024, 3])
    b_fc2 = tf.Variable(initial_value=initial)
    r_conv=tf.matmul(h_fc1_drop, W_fc2) + b_fc2

r_00, r_01, r_10, r_11 = tf.split(axis=1, num_or_size_splits=4, value=r_conv)
rot_trans = tf.maximum(tf.minimum(tf.concat([0.0803*r_00, 0.0803*r_01, tf.zeros_like(y_),  0.0803*r_10, 0.0803*r_11, tf.zeros_like(y_)], 1), 1.0),-1.0)
x_rot_trans = transformer(x_image, rot_trans, (24,24))

with tf.name_scope('Cost') as scope:
    loss = tf.reduce_mean((r_00 - tf.cos(y_))**2 + (r_01 - tf.sin(y_))**2 + (r_10 + tf.sin(y_))**2 + (r_11 - tf.cos(y_))**2)
with tf.name_scope('Optimizer') as scope:
    rot_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=rotate_scope.name)
    train_step = tf.train.AdamOptimizer(1e-3).minimize(loss, var_list=rot_vars)

cost_summary = tf.summary.scalar( 'cost', loss )

merged_summary_op = tf.summary.merge_all()
summary_writer = tf.summary.FileWriter("./tf_logs",graph=sess.graph)

sess.run(tf.global_variables_initializer())
saver = tf.train.Saver(var_list=rot_vars)
# saver.restore(sess, "tf_logs/rotate_model.ckpt")
# print("rotator model restored.")

bs = 45
for i in range(2000):
    batch = batch_utils.next_batch(bs, 0.95, True, True)

    if i%10 == 0:
        summary_str, ls, xt, xrt= sess.run([merged_summary_op, loss, x_trans, x_rot_trans], feed_dict={x:batch[0], y_: batch[7], keep_prob: 1.0})
        summary_writer.add_summary(summary_str,i)
        print("step %d, training loss %g"%(i, ls))

        for j in range(1):
            imsave('./tf_logs/' + str(i) + '_t'+str(j)+'.png',xt[j])
            imsave('./tf_logs/' + str(i) + '_rt'+str(j)+'.png',xrt[j])
            im = np.array(batch[0][j])
            im = im.reshape([224,224,3])
            imsave('./tf_logs/' + str(i) + '_b'+str(j)+'.png',im)

    train_step.run(feed_dict={x: batch[0], y_: batch[7], keep_prob: 0.5})

saver.save(sess, "tf_logs/rotate_model.ckpt")
summary_writer.close()
