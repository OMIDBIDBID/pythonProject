import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('image11.jpg',cv2.IMWRITE_EXR_TYPE)
plt.imshow(img,cmap='Accent_r',interpolation='bessel')
plt.plot([600,200],[200,300],'r',linewidth=90)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
