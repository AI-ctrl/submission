import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('data/Task_3.jpg',0)
_,thresh_binary_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imwrite("threshResults/Thresh_binary.jpg",thresh_binary_img)


adaptive_thresh_img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,55,1)
cv2.imwrite("threshResults/adaptive_thresh_img.jpg",adaptive_thresh_img)


