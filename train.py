import numpy as np
import cv2
from tensorflow.keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D
from keras.optimizers import Adam
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator

train_dir = r'C:\Users\tejay\OneDrive\Desktop\etc\src'
val_dir = r'C:\Users\tejay\OneDrive\Desktop\etc\src'
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
         train_dir,
         target_size=(48,48),
         batch_size=64,
         color_mode="grayscale",
         class_mode= 'categorical')
validation_generator = val_datagen.flow_from_directory(
        val_dir,
        target_size=(48,48),
        batch_size=64,
        color_mode="grayscale",
        class_mode= 'categorical')

emotion_model = Sequential()
emotion_model.add(Conv2D(32, kernel_size=(3, 3),activation= 'relu', input_shape=(48,48,1)))
emotion_model.add(Conv2D(64, kernel_size=(3,3),activation= 'relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout (0.25))
emotion_model.add(Conv2D(128, kernel_size=(3, 3),activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3),activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout (0.25))
emotion_model.add(Flatten())
emotion_model.add(Dense(1024,activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7,activation='softmax'))
 


emotion_model.compile(loss='categorical_crossentropy',optimizer=Adam(lr=0.0001),metrics=['accuracy'])

emotion_model_info = emotion_model.fit_generator(
        train_generator,
        steps_per_epoch=28709 // 64,
        epochs=50,# 50
        validation_data=validation_generator,
        validation_steps=7178 // 64)

emotion_model. save_weights('model.h5')