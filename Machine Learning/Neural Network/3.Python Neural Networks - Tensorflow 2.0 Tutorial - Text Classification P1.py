# This code has an error related to numpy 1.16.1 verson needed.


import tensorflow as tf
import keras
import numpy as np
import matplotlib.pyplot as plt

# Movie Rewiews Dataset
data = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=10000)  # Take only 10000 words that are more frequent

# Each of this Integers printed inside the 'train_images[0]' list, points to a single word.
print(train_data[0])

# Returns a dictionary that maps words to their integer indices.
word_index = data.get_word_index()

# Is used to create a new dictionary where each key-value pair in the word_index dictionary has the value incremented by 3.
word_index = {k:(v+3) for k, v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3

# We are reversing value with keys in our dictionary
reverse_word_index = dict([(value,key) for (key,value) in word_index.items()])

train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding="post",maxlen=250)
test_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding="post",maxlen=250)

# Overall, the purpose of this function is to take an encoded movie review as a sequence of integers and decode it back into a sequence of words
# for easier interpretation and analysis.
def decode_review(text):
    return " ".join([reverse_word_index.get(i, "?") for i in text])


# model down here
model = keras.Sequential()
model.add(keras.layers.Embedding(10000, 16))
model.add(keras.layers.GlobalAveragePooling1D(10000, 16))
model.add(keras.layers.Dense(16, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))

model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

x_val = train_data[:10000]
x_train = train_data[10000:]

y_val = train_labels[:10000]
y_train = train_labels[10000:]

fitModel = model.fit(x_train, y_train, epochs=40, batch_size=512, validation_data=(x_val, y_val), rebose=1)

results = model.evaluate(test_data, test_labels)

# print(results)
model.save("mymodel.h5")



