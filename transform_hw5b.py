#!/usr/bin/env python
import tensorflow as tf
from scipy.misc import imsave
import batch_utils
import numpy as np
import vgg16
from spatial_transformer import transformer
sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32, shape=[None, 224*224*3])
y_ = tf.placeholder(tf.float32, shape=[None, 3])

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

with tf.variable_scope('transformer_network') as trans_scope:
    x_image = tf.reshape(x, [-1,224,224,3])

    W_conv1 = weight_variable([5, 5, 3, 32])
    b_conv1 = bias_variable([32])
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    W_conv2 = weight_variable([5, 5, 32, 32])
    b_conv2 = bias_variable([32])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    # W_conv3 = weight_variable([5, 5, 32, 32])
    # b_conv3 = bias_variable([32])
    # h_conv3 = tf.nn.relu(conv2d(h_pool2, W_conv3) + b_conv3)
    # h_pool3 = max_pool_2x2(h_conv3)

    W_fc1 = weight_variable([56*56*32, 1024])
    b_fc1 = bias_variable([1024])
    h_pool2_flat = tf.reshape(h_pool2, [-1, 56*56*32])
    # h_pool3_flat = tf.reshape(h_pool3, [-1, 128*72*32])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    initial = np.array([0, 0, 0.0803])
    initial = initial.astype('float32')
    initial = initial.flatten()

    W_fc2 = tf.Variable(tf.truncated_normal([1024,3], stddev=1e-8))# tf.zeros([1024, 3]) # weight_variable([1024, 3])
    b_fc2 = tf.Variable(initial_value=initial)
    y_conv=tf.matmul(h_fc1_drop, W_fc2) + b_fc2

x_est, y_est, scale_out = tf.split(axis=1, num_or_size_splits=3, value=y_conv)
scale_est = tf.abs(scale_out)
trans = scale_est*tf.concat([tf.ones_like(x_est),tf.zeros_like(x_est),x_est,tf.zeros_like(x_est),tf.ones_like(x_est),y_est],1)
x_trans = transformer(x_image, trans, (24,24))

with tf.name_scope('Cost') as scope:
    x_act, y_act, scale = tf.split(axis=1, num_or_size_splits=3, value=y_)
    loss = tf.reduce_mean((x_act - x_est)**2 + (y_act - y_est)**2 + 200*(scale - scale_est)**2)
with tf.name_scope('Optimizer') as scope:
    trans_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=trans_scope.name)
    train_step = tf.train.AdamOptimizer(1e-3).minimize(loss, var_list=trans_vars)
with tf.name_scope('Accuracy') as scope:
    pix_accuracy = tf.reduce_mean(tf.sqrt((x_act - x_est)**2 + (y_act - y_est )**2))
    scale_accuracy = tf.reduce_mean(tf.abs(scale - scale_est))

# acc_summary = tf.summary.histogram( 'pix_accuracy', pix_accuracy )
acc_summary = tf.summary.scalar( 'pix_accuracy', pix_accuracy )
cost_summary = tf.summary.scalar( 'cost', loss )

merged_summary_op = tf.summary.merge_all()
summary_writer = tf.summary.FileWriter("./tf_logs",graph=sess.graph)

sess.run(tf.global_variables_initializer())
saver = tf.train.Saver(var_list=trans_vars)
# saver.restore(sess, "tf_logs/trans_model.ckpt")
# print("classification model restored.")

bs = 45
for i in range(4000):
    batch = batch_utils.next_batch(bs, 0.9 - i/2000, i > 1000, i > 300)

    if i%10 == 0:
        summary_str,p_acc, s_acc, xt, out = sess.run([merged_summary_op, pix_accuracy, scale_accuracy, x_trans, y_conv], feed_dict={x:batch[0], y_: batch[5], keep_prob: 1.0})
        summary_writer.add_summary(summary_str,i)
        print("step %d, training pixel accuracy %g, scale accuracy %g"%(i, p_acc, s_acc))

        for j in range(1):
            imsave('./tf_logs/' + str(i) + '_t'+str(j)+'.png',xt[j])
            im = np.array(batch[0][j])
            im = im.reshape([224,224,3])
            imsave('./tf_logs/' + str(i) + '_b'+str(j)+'.png',im)

    train_step.run(feed_dict={x: batch[0], y_: batch[5], keep_prob: 0.5})

saver.save(sess, "tf_logs/trans_model.ckpt")
summary_writer.close()
