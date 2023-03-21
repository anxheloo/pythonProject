# Write a function def convolve_grayscale_valid(images, kernel): that performs a valid convolution on grayscale images:
#
# images is a numpy.ndarray with shape (m, h, w) containing multiple grayscale images
#     m is the number of images
#     h is the height in pixels of the images
#     w is the width in pixels of the images
# kernel is a numpy.ndarray with shape (kh, kw) containing the kernel for the convolution
#     kh is the height of the kernel
#     kw is the width of the kernel
# You are only allowed to use two for loops; any other loops of any kind are not allowed
# Returns: a numpy.ndarray containing the convolved images




import matplotlib.pyplot as plt
import numpy as np
import math

def convolve_grayscale_valid(images, kernel):
    m, h, w = images.shape
    kh, kw = kernel.shape
    out_h, out_w = h - kh + 1, w - kw + 1
    output = np.zeros((m, out_h, out_w))


    for i in range(out_h):
        for j in range(out_w):
            output[:, i, j] = np.sum(images[:, i:i+kh, j:j+kw] * kernel, axis=(1,2))
    return output



dataset = np.load('C:/Users/HP280G1/Desktop/MNIST.npz')
images = dataset['X_train']
print(images.shape)
kernel = np.array([[1 ,0, -1], [1, 0, -1], [1, 0, -1]])
images_conv = convolve_grayscale_valid(images, kernel)
print(images_conv.shape)

plt.imshow(images[0], cmap='gray')
plt.show()
plt.imshow(images_conv[0], cmap='gray')
plt.show()