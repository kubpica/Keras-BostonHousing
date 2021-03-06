import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score

from keras.layers import Dropout

#set seed for reproduction purpose
from numpy.random import seed
seed(1)

from tensorflow import set_random_seed
set_random_seed(2)

import random as rn
rn.seed(12345)

import tensorflow as tf
tf.set_random_seed(1234)

#import seaborn as sns

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SG

from keras.datasets import boston_housing

(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

neural_model = Sequential([
    Dense(2, input_shape=(22,), activation="relu"), #why 22 inputs?
  #  Dense(2, activation="relu"),
    Dense(1, activation="relu")
])



#show summary of a model
neural_model.summary()

neural_model.compile(SGD(lr = .003), "mean_squared_error", \
                     metrics=["accuracy"])

np.random.seed(0)
run_hist_1 = neural_model.fit(data_train, target_train, epochs=4000,\
                              validation_data=(data_test, target_test), \
                              verbose=False, shuffle=False)

print("Training neural network...\n")

print('Accuracy over training data is ', \
      accuracy_score(target_train, neural_model.predict_classes(data_train)))

print('Accuracy over testing data is ', \
      accuracy_score(target_test, neural_model.predict_classes(data_test)))

conf_matrix = confusion_matrix(target_test, neural_model.predict_classes(data_test))
print(conf_matrix)

plt.plot(run_hist_1.history["loss"],'r', marker='.', label="Train Loss")
plt.plot(run_hist_1.history["val_loss"],'b', marker='.', label="Validation Loss")
plt.title("Train loss and validation error")
plt.legend()
plt.xlabel('Epoch'), plt.ylabel('Error')
plt.grid()

neural_network_d = Sequential()
neural_network_d.add(Dense(2, activation='relu', input_shape=(22,)))
neural_network_d.add(Dropout(0.1))
neural_network_d.add(Dense(1, activation='relu'))

neural_network_d.summary()

neural_network_d.compile(SGD(lr = .003), "mean_squared_error", metrics=["accuracy"])

run_hist_2 = neural_network_d.fit(data_train, target_train, epochs=4000, \
                                  validation_data=(data_test, target_test), \
                                  verbose=False, shuffle=False)

print("Training neural network w dropouts..\n")

print('Accuracy over training data is ', accuracy_score(target_train, \
                                                        neural_network_d.predict_classes(data_train)))

print('Accuracy over testing data is ', accuracy_score(target_test, \
                                                       neural_network_d.predict_classes(data_test)))

plt.show()

