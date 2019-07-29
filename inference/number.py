#!/usr/bin/env python
# coding: utf-8

# In[19]:

import sys
print (sys.argv[1])

from keras.datasets import mnist  
from keras.utils import np_utils
from PIL import Image
import numpy as np  
np.random.seed(10)  
(X_Train, y_Train), (X_Test, y_Test) = mnist.load_data()  

img = Image.open(sys.argv[1]).convert('L')
out = img.resize((28, 28))
out2=np.array(out)
X_Test[0] = out2

# Translation of data  
X_Train4D = X_Train.reshape(X_Train.shape[0], 28, 28, 1).astype('float32')  
X_Test4D = X_Test.reshape(X_Test.shape[0], 28, 28, 1).astype('float32') 


# In[20]:


# Standardize feature data  
X_Train4D_norm = X_Train4D / 255  
X_Test4D_norm = X_Test4D /255  
  
# Label Onehot-encoding  
y_TrainOneHot = np_utils.to_categorical(y_Train)  
y_TestOneHot = np_utils.to_categorical(y_Test) 


# In[21]:


from keras.models import Sequential  
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D 
import matplotlib.pyplot as plt  
import tensorflow as tf
model = tf.contrib.keras.models.load_model('/mnt/CNN_Mnist.h5')


# In[22]:


import matplotlib.pyplot as plt  
import tensorflow as tf

def show_train_history(train_history, train, validation):  
    plt.plot(train_history.history[train])  
    plt.plot(train_history.history[validation])  
    plt.title('Train History')  
    plt.ylabel(train)  
    plt.xlabel('Epoch')  
    plt.legend(['train', 'validation'], loc='upper left')  
    plt.show() 
    
def plot_images_labels_predict(images, labels, prediction, idx, num=10):  
    fig = plt.gcf()  
    fig.set_size_inches(12, 14)  
    if num > 25: num = 25  
    for i in range(0, num):  
        ax=plt.subplot(5,5, 1+i)  
        ax.imshow(images[idx], cmap='binary')  
        title = "l=" + str(labels[idx])  
        if len(prediction) > 0:  
            title = "l={},p={}".format(str(labels[idx]), str(prediction[idx]))  
        else:  
            title = "l={}".format(str(labels[idx]))  
        ax.set_title(title, fontsize=10)  
        ax.set_xticks([]); ax.set_yticks([])  
        idx+=1  
plt.show()  

scores = model.evaluate(X_Test4D_norm[0:2], y_TestOneHot[0:2])  
print()  
#print("\t[Info] Accuracy of testing data = {:2.1f}%".format(scores[1]*100.0))   

#print("\t[Info] Making prediction of X_Test4D_norm")  
prediction = model.predict_classes(X_Test4D_norm[0:10])  # Making prediction and save result to prediction  
print()  
#print("\t[Info] Show 10 prediction result (From 240):")  
print("%s\n" % (prediction[0:1]))
#plot_images_labels_predict(X_Test, y_Test, prediction, idx=1)  
#import pandas as pd
#print("\t[Info] Display Confusion Matrix:")
#print("%s\n" % pd.crosstab(y_Test, prediction, rownames=['label'], colnames=['predict']))


# In[ ]:




