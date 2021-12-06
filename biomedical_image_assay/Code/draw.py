import cv2 as cv
import numpy as np

blank = np.zeros((500,500,4),dtype='uint8')
blank[:] = 100,0,0,0
cv.rectangle(blank,(200,200),(blank.shape[1],blank.shape[0]),(200,200,0),thickness=-1,lineType = 1)
cv.putText(blank,'Hello,cv!',(100,300),cv.FONT_HERSHEY_SIMPLEX,
           1.2,(200,200,200),thickness=2)
cv.imshow('Blank',blank)
img = cv.imread('../../opencv-course/Resources/Photos/cat.jpg')
cv.imshow('Cat',img)
cv.waitKey(0)

