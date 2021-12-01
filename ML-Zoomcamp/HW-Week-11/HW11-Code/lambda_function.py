#!/usr/bin/env python
# coding: utf-8

# In[21]:



import tflite_runtime.interpreter as tflite

import numpy as np

from io import BytesIO
from urllib import request

from PIL import Image




interpreter = tflite.Interpreter(model_path='cats-dogs-v2.tflite')
interpreter.allocate_tensors()


# In[12]:


input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

classes = ['cats', 'dog']


def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result
# In[38]:


def preprocess_input(x):
    x /= 255
    return x


# # ANS Q3

# In[49]:

def predict(url):
    image = download_image(url)
    prep_image = prepare_image(image, (150,150))

    x = np.array(prep_image, dtype='float32')
    X = np.array([x])
    X = preprocess_input(X)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    return dict(zip(classes, float_predictions))

# In[20]:

# In[19]:





