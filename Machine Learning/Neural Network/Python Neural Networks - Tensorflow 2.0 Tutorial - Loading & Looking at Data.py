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

# We shrink down the values of pixels from 0-255 to 0-1
train_images = train_images/255.0
test_images = test_images/255.0

# This prints our image nr 7. of MNIST dataset , as an 28 * 28 array with pixels that show the form of a shirt.
print(train_images[7])

# We have 60000 images with 28 * 28 pixels
print(train_images.shape)
# We have 60000 labels for each image
print(train_labels.shape)
print(len(train_labels))
# 10000 test images with 28 * 28 pixels
print(test_images.shape)
# 10000 labels for each of those images
print(test_labels.shape)
print(len(test_labels))

# Plotting this image
plt.imshow(train_images[7], cmap=plt.cm.binary)
plt.show()

# Creating the Model| A sequential of layers in order
model = keras.Sequential([
    # Input layer, we flatten it to have it as a shape (784,)
    keras.layers.Flatten(input_shape=(28,28)),
    # First Hidden layer with 123 neurons using relu activation function
    keras.layers.Dense(128, activation="relu"),
    # Output layer with 10 neurons using softmax activation function
    keras.layers.Dense(10, activation="softmax")
])

'''
Loss function —This measures how accurate the model is during training. You want to minimize this function to "steer" the model in the right direction.
Optimizer —This is how the model is updated based on the data it sees and its loss function.
Metrics —Used to monitor the training and testing steps. The following example uses accuracy, the fraction of the images that are correctly classified.
'''
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train our model
model.fit(train_images, train_labels, epochs=5) # epochs give same images in different order 5 times

'''
Evaluate accuracy.
Next, compare how the model performs on the test dataset:
'''
test_loss , test_acc = model.evaluate(test_images, test_labels)

print("Tested Acc: ", test_acc)

'''
To verify that the data is in the correct format and that you're ready to build and train the network, 
let's display the first 25 images from the training set and display the class name below each image.
'''

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

# train_labels at index 20 is a number from 0-9 which corresponds with a class_names index in this case class_names[3] is dress.
# So the 21-th image is a dress with a dress label.
print(train_labels[20])
print(class_names[train_labels[20]])