# coding=utf-8
# Created by py on 2018/11/13.
"""
区别ll_key的不同
试图将函数和对应变量抽离，以函数的中间字节码作key，分析对应变量的误差
    **需要重写LLVM提取器**
"""


import tensorflow as tf
class LlvmCNN:
    def __init__(self, sequence_length, num_classes, vocab_size,
            embedding_size, filter_sizes, num_filters):

