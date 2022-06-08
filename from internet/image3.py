import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
#img=cv2.imread('image11.jpg',cv2.IMREAD_COLOR)
#plt.imshow(img,cmap='CMRmap',interpolation='bicubic')
img = mpimg.imread('image11.jpg')
plt.imshow(img)
plt.show()

px=img[(100:100),(200:200)]
print(px)
