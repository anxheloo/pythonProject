# Write a function def convolve_channels(images, kernel, padding='same', stride=(1, 1)): that performs a convolution on images with channels:
#
# images is a numpy.ndarray with shape (m, h, w, c) containing multiple images
#   m is the number of images
#   h is the height in pixels of the images
#   w is the width in pixels of the images
#   c is the number of channels in the image
# kernel is a numpy.ndarray with shape (kh, kw, c) containing the kernel for the convolution
#   kh is the height of the kernel
#   kw is the width of the kernel
# padding is either a tuple of (ph, pw), ‘same’, or ‘valid’
#   if ‘same’, performs a same convolution
#   if ‘valid’, performs a valid convolution
#   if a tuple:
#       ph is the padding for the height of the image
#       pw is the padding for the width of the image
# the image should be padded with 0’s
#   stride is a tuple of (sh, sw)
#       sh is the stride for the height of the image
#       sw is the stride for the width of the image
# You are only allowed to use two for loops; any other loops of any kind are not allowed
# Returns: a numpy.ndarray containing the convolved images


#!/usr/bin/env python3
"""      """

import numpy as np
import matplotlib.pyplot as plt


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """        """
    m, height, width, c = images.shape
    kh, kw, kc = kernel.shape
    sh, sw = stride

    if padding == 'same':
        if (kh % 2) == 1 and (kw % 2) == 1:
            ph = (kh - 1) // 2
            pw = (kw - 1) // 2
        else:
            ph = kh // 2
            pw = kw // 2

    elif padding == 'valid':
        ph = 0
        pw = 0
    else:
        ph, pw = padding

    images = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)), 'constant', constant_values=0)

    #     Convolution height and width

    ch = ((height + (2 * ph) - kh) // sh) + 1
    cw = ((width + (2 * pw) - kw) // sw) + 1

    convoluted = np.zeros((m, ch, cw))

    # Update Range
    i = 0
    for h in range(0, height + (2 * ph) - kh + 1, sh):
        j = 0
        for w in range(0, width + (2 * pw) - kw + 1, sw):
            output = np.sum(images[:, h: h + kh, w: w + kw, :] * kernel, axis=1).sum(axis=1).sum(axis=1)
            convoluted[:, i, j] = output
            j += 1
        i += 1
    return convoluted




dataset = np.load('C:/Users/HP280G1/Desktop/animals_1.npz')
images = dataset['data']
print(images.shape)
kernel = np.array([[[0, 0, 0], [-1, -1, -1], [0, 0, 0]], [[-1, -1, -1], [5, 5, 5], [-1, -1, -1]], [[0, 0, 0], [-1, -1, -1], [0, 0, 0]]])
images_conv = convolve_channels(images, kernel, padding='valid')
print(images_conv.shape)

plt.imshow(images[0])
plt.show()
plt.imshow(images_conv[0])
plt.show()