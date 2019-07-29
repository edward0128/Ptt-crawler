#export LD_LIBRARY_PATH=/usr/local/cuda/extras/CUPTI/lib64:/usr/local/nvidia/lib:/usr/local/nvidia/lib64;

from __future__ import print_function
 
import tensorflow as tf
 

hello = tf.constant('Hello, TensorFlow!')
 
# Start tf session
sess = tf.Session()
 
# Run the op
print(sess.run(hello))

