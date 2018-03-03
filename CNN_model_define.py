from keras.models import Sequential
from keras.layers import Convolution2D,MaxPooling2D, Flatten, Dense

def def_model():
  model = Sequential()

  model.add(Convolution2D(32, 3, 3, input_shape = (28, 28, 3), activation = 'relu'))
  model.add(MaxPooling2D(pool_size = (2, 2)))

  model.add(Convolution2D(32, 3, 3, activation = 'relu'))
  model.add(MaxPooling2D(pool_size = (2, 2)))

  model.add(Flatten())
  
  model.add(Dense(output_dim = 128, activation = 'relu'))
  model.add(Dense(output_dim = 256, activation = 'relu'))
  model.add(Dense(output_dim = 26, activation = 'sigmoid'))

  model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy'])

  return model
