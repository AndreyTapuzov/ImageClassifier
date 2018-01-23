from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from ResNet50.prediction_decoder import custom_decode_predictions
from keras.applications.resnet50 import preprocess_input

from keras.preprocessing import image
import numpy as np

class ResNet50Executor(object):
    def __init__(self, model_file_path = None):
        if(model_file_path == None or not isinstance(model_file_path, str)):
            raise ValueError("Model file path was not found")

        self.__model = load_model(model_file_path)

    def get_prediction_by_image_path(self, image_path, top = 1):
        img = image.load_img(image_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        x *= 1./255
        predictions = self.__model.predict(x)
        return custom_decode_predictions(predictions, top)
