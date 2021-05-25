from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow import keras
from tensorflow.keras import layers
import os
import pandas as pd
from pathlib import Path

os.chdir('/home/profesor/znakovi/Test')

# ucitavanje podataka iz odredenog direktorija

train_ds = image_dataset_from_directory(
    directory='/home/profesor/znakovi/Train',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48))


model = keras.Sequential([
    keras.Input(shape = (48,48,3)),
    layers.Conv2D(32, kernel_size=(3, 3),activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(16, kernel_size=(3, 3),activation='relu'),
    layers.Flatten(),
    layers.Dense(100, activation='relu'),
    layers.Dense(43, activation='softmax')
])
model.summary()

model.compile(loss='categorical_crossentropy',
optimizer='adam',
metrics=['accuracy'])



model.fit(train_ds, epochs=10, batch_size=32)
