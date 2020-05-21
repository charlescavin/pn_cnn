import tensorflow as tf
from tensorflow import keras
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
import numpy as np
import datetime as dt

img_paths = []
imgs = []
labels = []
IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128
IMAGE_DEPTH = 1
BATCH_SIZE = 15

# First load img files and labels (pe: Pleural Effusion)
pe_file = 'data/hdf/data_and_labels.h5'
pe = pd.read_hdf(pe_file, 'd')

print(f"pe shape: {pe.shape}")
print(f"pe head: {pe.head}")
print()

datagen = ImageDataGenerator(rescale=1./255)

train_generator = datagen.flow_from_dataframe(
    dataframe=pe,
    directory=None,
    x_col='path',
    y_col='Pleural Effusion',
    class_mode='binary',
    target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
    batch_size=BATCH_SIZE,
    validation_split=.2,
    subset='training'
)

validation_generator = datagen.flow_from_dataframe(
    dataframe=pe,
    directory=None,
    x_col='Paths',
    y_col='Labels',
    class_mode='binary',
    target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
    batch_size=BATCH_SIZE,
    validation_split=.2,
    subset='validation'
)

model = Sequential([
    tf.keras.layers.Conv2D(16, (3, 3),
                           activation='relu',
                           input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_DEPTH)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy', 'mse'])
