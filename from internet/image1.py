import cv2
import numpy as np
img=cv2.imread('image11.jpg',cv2.IMWRITE_EXR_TYPE)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
