#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tensorflow as tf

box = tf.Variable(tf.zeros([3,5],tf.int32))
box1 = tf.add(box,1)
tf.reduce_sum()

# 启动图后, 变量必须先经过`初始化` (init) op 初始化,
# 首先必须增加一个`初始化` op 到图中.
init_op = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init_op)
    print sess.run(box),'\n----\n',sess.run(box1)