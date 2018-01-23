from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from keras.models import load_model
from PIL import Image
import glob, os, csv
from ResNet50.prediction_decoder import custom_decode_predictions

def get_image_classes(file_path):
    class_names = []

    with open(file_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            for class_name in row:
                class_names.append(class_name)

    return class_names

class ModelTester(object):
    def __init__(self, model = ResNet50(weights='imagenet')):
        self._model = model
        self._images_data = []

    # Get all images with *.jpg extension in directory
    def _get_images_from_dir(self, directory_path):
        path_pattern = os.path.join(directory_path, '*.jpg')
        return glob.glob(path_pattern)

    def set_all_model_values(self, dataset_path, class_names):

        for class_name in class_names:
            class_folder_path = os.path.join(dataset_path, class_name)
            images_paths = self._get_images_from_dir(class_folder_path)

            for img_path in images_paths:
                img = image.load_img(img_path, target_size=(224, 224))

                x = image.img_to_array(img)
                x = np.expand_dims(x, axis=0)
                x = preprocess_input(x)
                x *= 1./255
                self._images_data.append(x)


    def get_resnet50_prediction(self):
        predictions = []

        for img_data in self._images_data:
            pred =  self._model.predict(img_data)
            predictions.append(custom_decode_predictions(pred, top=3)[0])

        return predictions

model = load_model("..\\Models\\ResNet50\\ResNet50_form_151_layer_trained_with_augmentation.h5")
resNet50ModelTester = ModelTester(model)

classes = get_image_classes('..\\Dataset\\FIDS30\\fruits.txt')
resNet50ModelTester.set_all_model_values('..\\Dataset\\FIDS30\\Test', classes)

predictions = resNet50ModelTester.get_resnet50_prediction()

pred_sum = 0
n = 30
for i in range(len(predictions)):
    print(str(i + 1)+ ". Справжній клас: \"" + classes[i] + "\" | передбачені класи : ", end=" ")

    if (classes[i] == predictions[i][0][0]):
        pred_sum += 1

    for j in range(2):
        print("\"" + predictions[i][j][0] +"\" : \"" + str(predictions[i][j][1]) + "\"", end = "; ")

    print("")
    print("---")

print("Right predicted : %d" % pred_sum)
print("Accuracy : %f" % (pred_sum / n))
