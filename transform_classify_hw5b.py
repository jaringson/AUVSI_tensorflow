#!/usr/bin/env python
import tensorflow as tf
from scipy.misc import imsave
import batch_utils
import numpy as np
import vgg16
from spatial_transformer import transformer
sess = tf.Session()

# placeholders
xs = tf.placeholder(tf.float32, shape=[None, 224*224*3], name="images")
let_ = tf.placeholder(tf.float32, shape=[None, 36])
sha_ = tf.placeholder(tf.float32, shape=[None, 13])
let_col_ = tf.placeholder(tf.float32, shape=[None, 10])
sha_col_ = tf.placeholder(tf.float32, shape=[None, 10])
keep_prob = tf.placeholder(tf.float32)
trans_randomness = tf.placeholder(tf.float32, shape=[None, 6])

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
vgg = vgg16.vgg16( x_image, 'vgg16_weights.npz', sess )

layers = [ 'conv5_1','conv5_2' ]
ops = [ getattr( vgg, x ) for x in layers ]

with tf.variable_scope('transformer_network') as trans_scope:
    vgg_conv5_1 = ops[0]
    W_conv1_l = weight_variable([3, 3, 512, 32])
    b_conv1_l = bias_variable([32])
    h_conv1_l = tf.nn.relu( tf.nn.conv2d( vgg_conv5_1, W_conv1_l, strides=[1, 1, 1, 1], padding='VALID' ) + b_conv1_l )
    h_conv1_l_flat = tf.reshape(h_conv1_l, [-1, 4608])

    W_fc1_l = weight_variable([4608, 64])
    b_fc1_l = bias_variable([64])
    h_fc1_l = tf.nn.relu(tf.matmul(h_conv1_l_flat, W_fc1_l) + b_fc1_l)

    # initial = np.array([[0.1, 0, 0], [0, 0.14, 0]])
    initial = np.array([[0.5, 0, 0], [0, 0.5, 0]])
    initial = initial.astype('float32')
    initial = initial.flatten()

    W_fc2_l = tf.Variable(tf.truncated_normal([64,6], stddev=1e-8))# tf.zeros([1024, 6]))
    b_fc2_l = tf.Variable(initial_value=initial)
    h_fc2_l = tf.matmul(h_fc1_l, W_fc2_l) + b_fc2_l + trans_randomness

x_trans = transformer(x_image, h_fc2_l, (24,24))

with tf.variable_scope('classifyer_network') as class_scope:
    W_conv1 = weight_variable([5, 5, 3, 32])
    b_conv1 = bias_variable([32])
    h_conv1 = tf.nn.relu(conv2d(x_trans, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    W_fc1 = weight_variable([6*6*64, 1024])
    b_fc1 = bias_variable([1024])
    h_pool2_flat = tf.reshape(h_pool2, [-1, 6*6*64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

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
    cross_entropies = tf.reduce_mean(-tf.reduce_sum(let_ * tf.log(let_conv), reduction_indices=[1])) + \
                      tf.reduce_mean(-tf.reduce_sum(sha_ * tf.log(sha_conv), reduction_indices=[1])) + \
                      tf.reduce_mean(-tf.reduce_sum(let_col_ * tf.log(let_col_conv), reduction_indices=[1])) + \
                      tf.reduce_mean(-tf.reduce_sum(sha_col_ * tf.log(sha_col_conv), reduction_indices=[1]))
with tf.name_scope('Optimizer'):
    class_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=class_scope.name)
    train_classifyer_step = tf.train.AdamOptimizer(5e-5).minimize(cross_entropies, var_list=class_vars)
    trans_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=trans_scope.name)
    train_transfomer_step = tf.train.AdamOptimizer(1e-7).minimize(cross_entropies, var_list=trans_vars)
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

acc_summary = tf.scalar_summary( 'letter accuracy', let_acc )
acc_summary = tf.scalar_summary( 'shape accuracy', sha_acc )
cost_summary = tf.scalar_summary( 'cost', cross_entropies )

merged_summary_op = tf.merge_all_summaries()
summary_writer = tf.train.SummaryWriter("./tf_logs",graph=sess.graph)
sess.run(tf.initialize_all_variables())
vgg.load_weights( 'vgg16_weights.npz', sess )

bs = 150
class_steps = 100
max_steps = 15000
m = 4.0/(class_steps - max_steps)
b = 0.75 - m*class_steps
print("step, shape_color, letter_color, shape, letter")
for i in range(max_steps):
    if i < class_steps:
        batch = batch_utils.next_batch(bs, 1, False, False)
        randness = np.array([-.4 + 0.015*np.random.randn(bs),0.015*np.random.randn(bs),0.03*np.random.randn(bs),0.015*np.random.randn(bs),-.36 + 0.015*np.random.randn(bs),0.03*np.random.randn(bs)]).transpose()
    else:
        batch = batch_utils.next_batch(bs, i*m + b, True, True)
        randness = np.zeros([bs,6])

    if i%10 == 0:
        summary_str,l,s,lc,sc = sess.run([merged_summary_op,let_acc, sha_acc,let_col_acc,sha_col_acc],feed_dict={xs:batch[0], let_: batch[1], sha_: batch[2], let_col_: batch[3], sha_col_: batch[4], keep_prob: 1.0, trans_randomness: randness})
        print("%d, %g, %g, %g, %g"%(i, sc,lc,s,l))
        summary_writer.add_summary(summary_str,i)

    if i%10 == 0 or (i > class_steps and i < class_steps + 30):
        xt, = sess.run([x_trans],feed_dict={xs: batch[0], keep_prob: 1.0, trans_randomness: randness})
        for j in range(1):
            imsave('./tf_logs/' + str(i) + '_t'+str(j)+'.png',xt[j])
            im = np.array(batch[0][j])
            im = im.reshape([143,256,3])
            imsave('./tf_logs/' + str(i) + '_b'+str(j)+'.png',im)

    if i < class_steps:
        train_classifyer_step.run(feed_dict={xs: batch[0], let_: batch[1], sha_: batch[2], let_col_: batch[3], sha_col_: batch[4], keep_prob: 0.5, trans_randomness: randness})
    elif i < 2*class_steps:
        train_transfomer_step.run(feed_dict={xs: batch[0], let_: batch[1], sha_: batch[2], let_col_: batch[3], sha_col_: batch[4], keep_prob: 0.75, trans_randomness: randness})
    else:
        train_step.run(feed_dict={xs: batch[0], let_: batch[1], sha_: batch[2], let_col_: batch[3], sha_col_: batch[4], keep_prob: 0.75, trans_randomness: randness})
