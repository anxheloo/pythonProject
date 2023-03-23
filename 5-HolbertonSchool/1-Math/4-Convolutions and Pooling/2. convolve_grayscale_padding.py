# Write a function def convolve_grayscale_padding(images, kernel, padding): that performs a convolution on grayscale images with custom padding:
#
# images is a numpy.ndarray with shape (m, h, w) containing multiple grayscale images
#   m is the number of images
#   h is the height in pixels of the images
#   w is the width in pixels of the images
# kernel is a numpy.ndarray with shape (kh, kw) containing the kernel for the convolution
#   kh is the height of the kernel
#   kw is the width of the kernel
# padding is a tuple of (ph, pw)
#   ph is the padding for the height of the image
#   pw is the padding for the width of the image
# the image should be padded with 0’s
# You are only allowed to use two for loops; any other loops of any kind are not allowed
# Returns: a numpy.ndarray containing the convolved images

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