#!/usr/bin/env python
import tensorflow as tf
from scipy.misc import imsave
import batch_utils
import numpy as np
import vgg16
from spatial_transformer import transformer
sess = tf.InteractiveSession()

# placeholders
xs = tf.placeholder(tf.float32, shape=[None, 224*224*3], name="images")
let_ = tf.placeholder(tf.float32, shape=[None, 36])
sha_ = tf.placeholder(tf.float32, shape=[None, 13])
let_col_ = tf.placeholder(tf.float32, shape=[None, 10])
sha_col_ = tf.placeholder(tf.float32, shape=[None, 10])
keep_prob = tf.placeholder(tf.float32)

# initialization functions
def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.2)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

# layer functions
def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

x_image = tf.reshape(xs, [-1,224,224,3])
# vgg = vgg16.vgg16( x_image, 'vgg16_weights.npz', sess )
#
# layers = [ 'conv5_1','conv5_2' ]
# ops = [ getattr( vgg, x ) for x in layers ]

with tf.variable_scope('transformer_network') as trans_scope:
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

    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    initial = np.array([0, 0, 112])
    initial = initial.astype('float32')
    initial = initial.flatten()

    W_fc2 = tf.Variable(tf.truncated_normal([1024,3], stddev=1e-8))# tf.zeros([1024, 3]) # weight_variable([1024, 3])
    b_fc2 = tf.Variable(initial_value=initial)
    y_conv=tf.matmul(h_fc1_drop, W_fc2) + b_fc2

x_est, y_est, scale_out = tf.split(axis=1, num_or_size_splits=3, value=y_conv)
scale_est = tf.abs(scale_out)*0.0803/112
trans = tf.maximum(tf.minimum(tf.concat([scale_est*tf.ones_like(x_est), tf.zeros_like(x_est), x_est/112,  tf.zeros_like(x_est), scale_est*tf.ones_like(x_est), y_est/112], 1), 1.0),-1.0)
x_trans = transformer(x_image, trans, (24,24))

with tf.variable_scope('rotator_network') as rotate_scope:
    W_conv1 = weight_variable([5, 5, 3, 32])
    b_conv1 = bias_variable([32])
    h_conv1 = tf.nn.relu(conv2d(x_trans, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    W_conv2 = weight_variable([5, 5, 32, 32])
    b_conv2 = bias_variable([32])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    W_fc1 = weight_variable([6*6*32, 1024])
    b_fc1 = bias_variable([1024])
    h_pool2_flat = tf.reshape(h_pool2, [-1, 6*6*32])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    initial = np.array([1, 0, 0, 1])
    initial = initial.astype('float32')
    initial = initial.flatten()

    W_fc2 = tf.Variable(tf.truncated_normal([1024,4], stddev=1e-8))# tf.zeros([1024, 3]) # weight_variable([1024, 3])
    b_fc2 = tf.Variable(initial_value=initial)
    r_conv=tf.matmul(h_fc1_drop, W_fc2) + b_fc2

r_00, r_01, r_10, r_11 = tf.split(axis=1, num_or_size_splits=4, value=r_conv)
rot_trans = tf.maximum(tf.minimum(tf.concat([scale_est*r_00, scale_est*r_01, x_est/112,  scale_est*r_10, scale_est*r_11, y_est/112], 1), 1.0),-1.0)
x_rot_trans = transformer(x_image, rot_trans, (24,24))

with tf.variable_scope('classifyer_network') as class_scope:
    W_conv1 = weight_variable([5, 5, 3, 32])
    b_conv1 = bias_variable([32])
    h_conv1 = tf.nn.relu(conv2d(x_rot_trans, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    W_fc1 = weight_variable([6 * 6 * 64, 1024])
    b_fc1 = bias_variable([1024])
    h_pool2_flat = tf.reshape(h_pool2, [-1, 6 * 6 * 64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    # keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    with tf.variable_scope("letter"):
        W_fc2 = tf.get_variable( "W", [1024, 36], tf.float32,
                                  tf.random_normal_initializer( stddev=np.sqrt(2 / np.prod(h_fc1_drop.get_shape().as_list()[1:])) ) ) # weight_variable([1024, 36])
        b_fc2 = bias_variable([36])
        let_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

    with tf.variable_scope("shape"):
        W_fc2 = tf.get_variable( "W", [1024, 13], tf.float32,
                                  tf.random_normal_initializer( stddev=np.sqrt(2 / np.prod(h_fc1_drop.get_shape().as_list()[1:])) ) ) # weight_variable([1024, 36])
        b_fc2 = bias_variable([13])
        sha_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

    with tf.variable_scope("letter_color"):
        W_fc2 = tf.get_variable( "W", [1024, 10], tf.float32,
                                  tf.random_normal_initializer( stddev=np.sqrt(2 / np.prod(h_fc1_drop.get_shape().as_list()[1:])) ) ) # weight_variable([1024, 36])
        b_fc2 = bias_variable([10])
        let_col_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

    with tf.variable_scope("shape_color"):
        W_fc2 = tf.get_variable( "W", [1024, 10], tf.float32,
                                  tf.random_normal_initializer( stddev=np.sqrt(2 / np.prod(h_fc1_drop.get_shape().as_list()[1:])) ) ) # weight_variable([1024, 36])
        b_fc2 = bias_variable([10])
        sha_col_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

with tf.name_scope('Cost'):
    cross_entropies = tf.reduce_mean(-tf.reduce_sum(let_ * tf.log(tf.clip_by_value(let_conv,1e-10,1)), axis=[1])) + \
                      .5 * tf.reduce_mean(-tf.reduce_sum(sha_ * tf.log(tf.clip_by_value(sha_conv,1e-10,1)), axis=[1])) + \
                      .25 * tf.reduce_mean(-tf.reduce_sum(let_col_ * tf.log(tf.clip_by_value(let_col_conv,1e-10,1)), axis=[1])) + \
                      .05 * tf.reduce_mean(-tf.reduce_sum(sha_col_ * tf.log(tf.clip_by_value(sha_col_conv,1e-10,1)), axis=[1]))

    loss = cross_entropies + 0.1*tf.reduce_mean(tf.abs(tf.matrix_determinant(tf.reshape(r_conv,[-1,2,2])) - 1 ))
with tf.name_scope('Optimizer'):
    trans_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=trans_scope.name)
    train_transfomer_step = tf.train.AdamOptimizer(5e-7).minimize(cross_entropies, var_list=trans_vars)

    rot_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=rotate_scope.name)
    train_rotate_step = tf.train.AdamOptimizer(1e-5).minimize(loss, var_list=rot_vars)

    class_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=class_scope.name)
    train_classifyer_step = tf.train.AdamOptimizer(1e-6).minimize(cross_entropies, var_list=class_vars)

    train_step = tf.train.AdamOptimizer(1e-8).minimize(cross_entropies)
with tf.name_scope('Accuracy'):
    let_correct_prediction = tf.equal(tf.argmax(let_conv,1), tf.argmax(let_,1))
    let_acc = tf.reduce_mean(tf.cast(let_correct_prediction, tf.float32))
    sha_correct_prediction = tf.equal(tf.argmax(sha_conv,1), tf.argmax(sha_,1))
    sha_acc = tf.reduce_mean(tf.cast(sha_correct_prediction, tf.float32))
    let_col_correct_prediction = tf.equal(tf.argmax(let_col_conv,1), tf.argmax(let_col_,1))
    let_col_acc = tf.reduce_mean(tf.cast(let_col_correct_prediction, tf.float32))
    sha_col_correct_prediction = tf.equal(tf.argmax(sha_col_conv,1), tf.argmax(sha_col_,1))
    sha_col_acc = tf.reduce_mean(tf.cast(sha_col_correct_prediction, tf.float32))

acc_summary = tf.summary.scalar( 'letter accuracy', let_acc )
acc_summary = tf.summary.scalar( 'shape accuracy', sha_acc )
cost_summary = tf.summary.scalar( 'cost', cross_entropies )

merged_summary_op = tf.summary.merge_all()
summary_writer = tf.summary.FileWriter("./tf_logs",graph=sess.graph)
sess.run(tf.global_variables_initializer())
# vgg.load_weights( 'vgg16_weights.npz', sess )

c_saver = tf.train.Saver(var_list=class_vars)
c_saver.restore(sess, "tf_logs/class_model.ckpt")
print("classification model restored.")

# r_saver = tf.train.Saver(var_list=rot_vars)
# r_saver.restore(sess, "tf_logs/rotate_model.ckpt")
# print("rotator model restored.")

t_saver = tf.train.Saver(var_list=trans_vars)
t_saver.restore(sess, "tf_logs/trans_model.ckpt")
print("transformer model restored.")

saver = tf.train.Saver()

bs = 50
max_steps = 3000

print("step, shape_color, letter_color, shape, letter")
for i in range(max_steps):
    batch = batch_utils.next_batch(bs, 0, True, True)

    if i%1 == 0:
        summary_str,l,s,lc,sc = sess.run([merged_summary_op,let_acc, sha_acc,let_col_acc,sha_col_acc],feed_dict={xs:batch[0], let_: batch[1], sha_: batch[2], let_col_: batch[3], sha_col_: batch[4], keep_prob: 1.0})
        print("%d, %g, %g, %g, %g"%(i, sc,lc,s,l))
        summary_writer.add_summary(summary_str,i)

    if i%10 == 0 or (i > max_steps/2 and i < max_steps/2 + 30):
        xt, xrt = sess.run([x_trans, x_rot_trans],feed_dict={xs: batch[0], keep_prob: 1.0})
        for j in range(1):
            imsave('./tf_logs/' + str(i) + '_t'+str(j)+'.png',xt[j])
            imsave('./tf_logs/' + str(i) + '_rt'+str(j)+'.png',xrt[j])
            im = np.array(batch[0][j])
            im = im.reshape([224,224,3])
            imsave('./tf_logs/' + str(i) + '_b'+str(j)+'.png',im)

    if i < max_steps/2:
        train_rotate_step.run(feed_dict={xs: batch[0], let_: batch[1], sha_: batch[2], let_col_: batch[3], sha_col_: batch[4], keep_prob: 0.5})
    else:
        train_step.run(feed_dict={xs: batch[0], let_: batch[1], sha_: batch[2], let_col_: batch[3], sha_col_: batch[4], keep_prob: 0.75})

saver.save(sess, "tf_logs/whole_model.ckpt")
summary_writer.close()
