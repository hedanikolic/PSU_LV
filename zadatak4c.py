import matplotlib.pyplot as plt
import numpy as np
import skimage.io


img = skimage.io.imread('tiger.png', as_gray=True)
plt.figure(1)

height = img.shape[0]
width = img.shape[1]
matrica = np.ones((height, width))

img1 = np.zeros((height, width))

for j in range(0, width):
    img1[:, width-j-1] = img[:,j]


plt.imshow(img1, cmap='gray', vmin=0, vmax=255)

plt.show()