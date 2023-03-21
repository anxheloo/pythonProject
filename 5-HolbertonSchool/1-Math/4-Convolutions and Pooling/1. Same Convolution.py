# Write a function def convolve_grayscale_same(images, kernel): that performs a same convolution on grayscale images:
#
# images is a numpy.ndarray with shape (m, h, w) containing multiple grayscale images
#     m is the number of images
#     h is the height in pixels of the images
#     w is the width in pixels of the images
# kernel is a numpy.ndarray with shape (kh, kw) containing the kernel for the convolution
#     kh is the height of the kernel
#     kw is the width of the kernel
# if necessary, the image should be padded with 0’s
# You are only allowed to use two for loops; any other loops of any kind are not allowed
# Returns: a numpy.ndarray containing the convolved images




import matplotlib.pyplot as plt
import numpy as np
import math

def convolve_grayscale_same(images, kernel):
    m, h, w = images.shape
    kh, kw = kernel.shape

    pad_h = int((kh - 1) / 2)
    pad_w = int((kw - 1) / 2)

    #Ready made function to add 0 to the images :   images is the input grayscale image with shape (m, h, w),
    # where m is the number of images, h is the height in pixels of the images, and w is the width in pixels of the images
    #The tuple ((0,0), (pad_h,pad_h), (pad_w,pad_w)) specifies the amount of padding to add to each dimension of the image.
    # The first element (0,0) indicates that no padding is added to the first dimension, which represents the number of images
    padded_images = np.pad(images, ((0, 0), (pad_h, pad_h), (pad_w, pad_w)), mode='constant')
    output = np.zeros((m, h, w))


    for i in range(h):
        for j in range(w):
            output[:, i, j] = np.sum(padded_images[:, i:i+kh, j:j+kw] * kernel, axis=(1,2))
    return output




dataset = np.load('C:/Users/HP280G1/Desktop/MNIST.npz')
images = dataset['X_train']
print(images.shape)
kernel = np.array([[1 ,0, -1], [1, 0, -1], [1, 0, -1]])
images_conv = convolve_grayscale_same(images, kernel)
print(images_conv.shape)

plt.imshow(images[0], cmap='gray')
plt.show()
plt.imshow(images_conv[0], cmap='gray')
plt.show()