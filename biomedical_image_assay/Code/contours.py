import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img =  cv.imread('../../opencv-course/Resources/Photos/cats.jpg')

blank = np.zeros((500,300),dtype='uint8')
plt.imshow(blank)
plt.title('Opencv')
plt.show()

cv.waitKey(0)