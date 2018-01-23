from time import time

from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from ResNet50.prediction_decoder import custom_decode_predictions

test_data_gen = ImageDataGenerator(
                                   rescale=1./255,
                                   rotation_range=90,
                                   vertical_flip=True,
                                   horizontal_flip=True,
                                   zoom_range=0.2,
                                   height_shift_range=0.2,
                                   width_shift_range=0.2,
                                   channel_shift_range=0.2
                                   )

test_generator = test_data_gen.flow_from_directory(
     "D:\\!Karazina\\5_Course\\Diploma\\Programm\\Dataset\\FIDS30\\Test2",
    target_size=(224, 224),
    batch_size=1,
    class_mode='binary',
    #save_to_dir='..\\Dataset\AugmentedTestImages',
   # save_prefix='aug',
    #save_format='jpeg'
)


model = load_model("..\\Models\\ResNet50\\ResNet50_form_151_layer_trained_with_augmentation.h5")

num_of_runs = 10
avg_prediction_time_sum, loss_sum, accuracy_sum = 0, 0, 0

for i in range(num_of_runs):
    start_time = time()
    predicted_scores = model.predict_generator(test_generator, len(test_generator))
    end_time = time()

    avg_prediction_time_sum += round(end_time - start_time, 3) / len(test_generator)
    #decoded_prediction_scrores = custom_decode_predictions(predicted_scores, top = 1)
    evaluated_scores = model.evaluate_generator(test_generator, len(test_generator))
    loss_sum += evaluated_scores[0]
    accuracy_sum += evaluated_scores[1]


print("Loss: ", loss_sum / num_of_runs, "Accuracy: ", accuracy_sum / num_of_runs)
print("Avg prediction time per image :", avg_prediction_time_sum / num_of_runs, " sec")
#print(len(decoded_prediction_scrores))
#for d in decoded_prediction_scrores:
#    print(d[0][0], " : ", d[0][1])
