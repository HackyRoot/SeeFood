import tensorflow as tf
import requests
import json
import numpy as np

MODEL_URI = 'http://localhost:8501/v1/models/seefood:predict'
SIZE = 224
CLASSES = ['Hot Dog', 'Not Hot Dog']

def get_prediction(img_path):
    img = tf.keras.preprocessing.image.load_img(
        img_path, target_size=(SIZE, SIZE))

    img = tf.keras.preprocessing.image.img_to_array(img)
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    img = np.expand_dims(img, axis=0)

    data = json.dumps({
        'instances': img.tolist()
    })

    response = requests.post(MODEL_URI, data=data.encode())
    result = json.loads(response.text)
    prediction = np.argmax(result['predictions'][0], axis=-1)
    class_name = CLASSES[prediction]
    # print(class_name)
    return class_name