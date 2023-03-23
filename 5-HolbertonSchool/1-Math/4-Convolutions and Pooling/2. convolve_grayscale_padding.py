#!/usr/bin/env python3
"""      """

import numpy as np
import matplotlib.pyplot as plt


def convolve_grayscale_padding(images, kernel, padding):
    """        """
    m, height, width = images.shape
    kh, kw = kernel.shape

    ph, pw = padding
    images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 'constant', constant_values=0)

    #     Convolution height and width
    ch = height + (2 * ph) - kh + 1
    cw = width + (2 * pw) - kw + 1

    convoluted = np.zeros((m, ch, cw))

    for h in range(ch):
        for w in range(cw):
            output = np.sum(images[:, h: h + kh, w: w + kw] * kernel, axis=1).sum(axis=1)
            convoluted[:, h, w] = output
    return convoluted




dataset = np.load('C:/Users/HP280G1/Desktop/MNIST.npz')
images = dataset['X_train']
print(images.shape)
kernel = np.array([[1 ,0, -1], [1, 0, -1], [1, 0, -1]])
images_conv = convolve_grayscale_padding(images, kernel, (2, 4))
print(images_conv.shape)

plt.imshow(images[0], cmap='gray')
plt.show()
plt.imshow(images_conv[0], cmap='gray')
plt.show()