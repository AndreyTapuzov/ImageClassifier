from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model

#creating image data generator
train_data_gen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=90,
                                   vertical_flip=True,
                                   horizontal_flip=True,
                                   zoom_range=0.2,
                                   height_shift_range=0.2,
                                   width_shift_range=0.2,
                                   channel_shift_range=0.2)

train_generator = train_data_gen.flow_from_directory(
     "..\\Dataset\\FIDS30\\FIDS30_Train",
    target_size=(224, 224),
    batch_size=10,
    class_mode='binary',
)

model = load_model("..\\Models\\ResNet50\\ResNet50_with_top_trained_fc_layer_with_augmentation.h5")

for layer in model.layers[:151]:
   layer.trainable = False
for layer in model.layers[151:]:
   layer.trainable = True

#  recompile the model for these modifications to take effect
#  and use SGD with a low learning rate
from keras.optimizers import SGD
model.compile(optimizer=SGD(lr=0.0001, momentum=0.90), loss='sparse_categorical_crossentropy', metrics=['accuracy'])


history = model.fit_generator(train_generator, steps_per_epoch=91, epochs=15)

model.save("..\\Models\\ResNet50\\ResNet50_form_151_layer_trained_with_augmentation.h5")