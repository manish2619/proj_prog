import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

