import numpy as np
import cv2

x=cv2.imread('t5.jpg')
y=cv2.imread('t4.jpg')
x[0:y.shape[0],0:y.shape[1]]=y
cv2.imshow('x',x)
cv2.waitKey(0)
cv2.destroyAllWindows()
