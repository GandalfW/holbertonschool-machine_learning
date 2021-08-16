#!/usr/bin/env python3
'''
0. Placeholders
'''
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

def create_placeholders(nx, classes):
    '''
    Returns two placeholders, x and y, for the neural network
    '''
    return tf.placeholder(float, shape=(None, nx), name='x'), tf.placeholder(float, shape=(None, classes), name='y')
