import numpy as np
import matplotlib.pyplot as plt

def convolve(images, kernels, padding='same', stride=(1, 1)):
    m, h, w, c = images.shape
    kh, kw, c, nc = kernels.shape
    sh, sw = stride

    if padding == 'same':
        ph = int(np.ceil((sh * (h - 1) + kh - h) / 2))
        pw = int(np.ceil((sw * (w - 1) + kw - w) / 2))
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    images_padded = np.pad(images, ((0,0), (ph,ph),(pw,pw), (0,0)), 'constant', constant_values=0)

    oh = int((h + 2 * ph - kh) / sh + 1)
    ow = int((w + 2 * pw - kw) / sw + 1)
    output = np.zeros((m, oh, ow, nc))

    for i in range(m):
        for j in range(oh):
            for k in range(ow):
                for l in range(nc):
                    output[i, j, k, l] = np.sum(images_padded[i,
                        j*sh:j*sh+kh, k*sw:k*sw+kw, :] * kernels[:, :, :, l])

    return output



dataset = np.load('C:/Users/HP280G1/Desktop/animals_1.npz')
images = dataset['data']
print(images.shape)
kernels = np.array([
    [
        [[0, 1, 1], [0, 1, 1], [0, 1, 1]],
        [[-1, 0, 1],[-1, 0, 1], [-1, 0, 1]],
        [[0, -1, 1], [0, -1, 1], [0, -1, 1]]
    ],

    [
        [[-1, 1, 0], [-1, 1, 0], [-1, 1, 0]],
         [[5, 0, 0], [5, 0, 0], [5, 0, 0]],
         [[-1, -1, 0], [-1, -1, 0], [-1, -1, 0]]
    ],

    [
         [[0, 1, -1], [0, 1, -1], [0, 1, -1]],
         [[-1, 0, -1], [-1, 0, -1], [-1, 0, -1]],
         [[0, -1, -1], [0, -1, -1], [0, -1, -1]]
    ]
])

images_conv = convolve(images, kernels, padding='valid')
print(images_conv.shape)

plt.imshow(images[0])
plt.show()
plt.imshow(images_conv[0, :, :, 0])
plt.show()
plt.imshow(images_conv[0, :, :, 1])
plt.show()
plt.imshow(images_conv[0, :, :, 2])
plt.show()