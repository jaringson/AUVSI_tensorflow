import tensorflow as tf
import background
sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32, shape=[None, 1024*570*3])
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

with tf.name_scope('Wx_B') as scope:
    x_image = tf.reshape(x, [-1,1024,570,3])
    h_pool0 = tf.nn.max_pool(x_image, ksize=[1, 4, 4, 1], strides=[1, 4, 4, 1], padding='SAME')

    W_conv1 = weight_variable([5, 5, 3, 32])
    b_conv1 = bias_variable([32])
    h_conv1 = tf.nn.relu(conv2d(h_pool0, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    W_conv2 = weight_variable([5, 5, 32, 32])
    b_conv2 = bias_variable([32])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    # W_conv3 = weight_variable([5, 5, 32, 32])
    # b_conv3 = bias_variable([32])
    # h_conv3 = tf.nn.relu(conv2d(h_pool2, W_conv3) + b_conv3)
    # h_pool3 = max_pool_2x2(h_conv3)

    W_fc1 = weight_variable([64*36*32, 1024])
    b_fc1 = bias_variable([1024])
    h_pool2_flat = tf.reshape(h_pool2, [-1, 64*36*32])
    # h_pool3_flat = tf.reshape(h_pool3, [-1, 128*72*32])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    W_fc2 = weight_variable([1024, 3])
    b_fc2 = bias_variable([3])
    y_conv=tf.matmul(h_fc1_drop, W_fc2) + b_fc2

with tf.name_scope('Cost') as scope:
  x_act, y_act, ang = tf.split(1, 3, y_)
  x_est, y_est, ang_est = tf.split(1, 3, y_conv)
  loss = tf.reduce_mean((x_act - x_est)**2 + (y_act - y_est)**2 + 0.44*(ang - ang_est)**2)
  #loss = tf.reduce_mean(tf.reduce_sum(tf.subtract(y_ , y_conv)**2, reduction_indices=[1]))
with tf.name_scope('Optimizer') as scope:
  train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)
with tf.name_scope('Accuracy') as scope:
  pix_accuracy = tf.reduce_mean(tf.sqrt((x_act - x_est)**2 + (y_act - y_est )**2))
  ang_accuracy = tf.reduce_mean(tf.abs(ang - ang_est))

acc_summary = tf.scalar_summary( 'pix_accuracy', pix_accuracy )
cost_summary = tf.scalar_summary( 'cost', loss )

merged_summary_op = tf.merge_all_summaries()
summary_writer = tf.train.SummaryWriter("./tf_logs",graph=sess.graph)
sess.run(tf.initialize_all_variables())
for i in range(2000):
  #batch = mnist.train.next_batch(50)
  batch = background.next_batch(150)
  #print len(batch[0][0])
  #print len(batch_2[1][0])
  if i%10 == 0:
    p_acc, a_acc = sess.run([pix_accuracy, ang_accuracy], feed_dict={x:batch[0], y_: batch[5], keep_prob: 1.0})
    if i%100 == 0:
        print("step %d, training pixel accuracy %g, angle accuracy %g"%(i, p_acc, a_acc))
    summary_str, = sess.run([merged_summary_op],feed_dict={x: batch[0], y_: batch[5], keep_prob: 0.5})
    summary_writer.add_summary(summary_str,i)
  train_step.run(feed_dict={x: batch[0], y_: batch[5], keep_prob: 0.5})
