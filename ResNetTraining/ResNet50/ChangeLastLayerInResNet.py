from keras.applications.resnet50 import ResNet50
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D

# create the base pre-trained model
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224,224,3))

# add a global spatial average pooling layer
x = base_model.output
x = GlobalAveragePooling2D()(x)
# and a fully-connected layer
predictions = Dense(30, activation='softmax')(x)

# create model to train
model = Model(inputs=base_model.input, outputs=predictions)

# set only the top layers to train (which were randomly initialized)
# i.e. freeze all convolutional layers
for layer in base_model.layers:
    layer.trainable = False

# compile the model
model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy')


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
    class_mode='binary'
)

# train the model on the new data for a few epochs
model.fit_generator(train_generator, steps_per_epoch=91, epochs=3)

# save trained model
model.save("..\\Models\\ResNet50\\ResNet50_with_top_trained_fc_layer_with_augmentation.h5")