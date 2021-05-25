from keras.preprocessing.image import img_to_array
from keras.models import load_model
from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage import color
import matplotlib.image as mpimg
import numpy as np
from tensorflow import keras
from sklearn.datasets import fetch_openml

X,y = fetch_openml('mnist_784', version=1,return_X_y=True,as_frame=False)

img = X[0, :]
img = img.reshape((28, 28))
plt.imshow(img, cmap='gray')
plt.show()

img = mpimg.imread(X)
img = color.rgb2gray(img)
img = resize(img, (28, 28))


plt.figure()
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()


img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()


# TODO: ucitaj model

model = keras.models.load_model('/home/profesor/Downloads')

# TODO: napravi predikciju 

classes = model.predict(x_test, batch_size=128)

# TODO: ispis rezultat
print("------------------------")
print(classes)


