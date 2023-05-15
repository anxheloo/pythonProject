# TensorFlow and tf.keras
import keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Each image is mapped to a single label. Since the class names are not included with the dataset, store them here to use later when plotting the images:
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# We shrink down the values of pixels from 0-255 to 0-1 for better performance
train_images = train_images/255.0
test_images = test_images/255.0

# Plotting this image
plt.imshow(train_images[7], cmap=plt.cm.binary)
plt.show()

# Creating the Model| A sequential of layers in order
model = keras.Sequential([
    # Input layer, we flatten it to have it as a shape (784,)
    keras.layers.Flatten(input_shape=(28,28)),
    # First Hidden layer with 128 neurons using relu activation function
    keras.layers.Dense(128, activation="relu"),
    # Output layer with 10 neurons using softmax activation function
    keras.layers.Dense(10, activation="softmax")
])

'''
Loss function — This measures how accurate the model is during training. You want to minimize this function to "steer" the model in the right direction.
Optimizer — This is how the model is updated based on the data it sees and its loss function.
Metrics — Used to monitor the training and testing steps. The following example uses accuracy, the fraction of the images that are correctly classified.
'''
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train our model
model.fit(train_images, train_labels, epochs=5) # epochs give same images in different order 5 times

# This prints the probabilities of images being a label from 0-9.
prediction = model.predict(test_images)
print(prediction)

# We are going to take the index of max value and say this is the predicted value
# print(class_names[np.argmax(prediction[0])])

# See the image what it actualy is versus the predicted from the model
for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel("Actual: " + class_names[test_labels[i]])
    plt.title("Prediction " + class_names[np.argmax(prediction[i])])
    plt.show()

