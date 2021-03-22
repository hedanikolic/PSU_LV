import matplotlib.pyplot as plt
import numpy as np
import skimage.io


img = skimage.io.imread('tiger.png', as_gray=True)
plt.figure(1)

height = img.shape[0]
width = img.shape[1]
matrica = np.ones((height, width))*100

plt.imshow(img+matrica, cmap='gray', vmin=0, vmax=255)

plt.show()