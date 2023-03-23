# Write a function def pool(images, kernel_shape, stride, mode='max'): that performs pooling on images:
#
# images is a numpy.ndarray with shape (m, h, w, c) containing multiple images
#   m is the number of images
#   h is the height in pixels of the images
#   w is the width in pixels of the images
#   c is the number of channels in the image
# kernel_shape is a tuple of (kh, kw) containing the kernel shape for the pooling
#   kh is the height of the kernel
#   kw is the width of the kernel
# stride is a tuple of (sh, sw)
#   sh is the stride for the height of the image
#   sw is the stride for the width of the image
# mode indicates the type of pooling
#   max indicates max pooling
#   avg indicates average pooling
# You are only allowed to use two for loops; any other loops of any kind are not allowed
# Returns: a numpy.ndarray containing the pooled images



#!/usr/bin/env python3
"""      """

import numpy as np
import matplotlib.pyplot as plt


def pool(images, kernel_shape, stride, mode='max'):
    """        """
    m, height, width, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    pool_h = ((height - kh) // sh) + 1
    pool_w = ((width - kw) // sw) + 1
    pooled = np.zeros((m, pool_h, pool_w, c))

    i = 0
    for h in range(0, height - kh + 1, sh):
        j = 0
        for w in range(0, width - kw + 1, sw):
            if mode == 'max':
                output = np.max(images[:, h: h + kh, w: w + kw, :], axis=(1, 2))
            if mode == 'avg':
                output = np.average(images[:, h: h + kh, w: w + kw, :], axis=(1, 2))

            pooled[:, i, j, :] = output
            j += 1
        i += 1

    return pooled



dataset = np.load('C:/Users/HP280G1/Desktop/animals_1.npz')
images = dataset['data']
print(images.shape)
images_pool = pool(images, (2, 2), (2, 2), mode='avg')
print(images_pool.shape)

plt.imshow(images[0])
plt.show()
plt.imshow(images_pool[0] / 255)
plt.show()