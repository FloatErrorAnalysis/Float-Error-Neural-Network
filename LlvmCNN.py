# Created by py on 2018/11/13.

import tensorflow as tf
class LlvmCNN:
    def __init__(self, sequence_length, num_classes, vocab_size,
            embedding_size, filter_sizes, num_filters):
