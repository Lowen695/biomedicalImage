import cv2 as cv
import matplotlib.pyplot as plt

img =  cv.imread('../../opencv-course/Resources/Photos/cats.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray_hist = cv.calcHist([gray],[0],None,[10],[0,256])

plt.figure()
plt.title('Fig_hist')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist,c='red ')
plt.show()