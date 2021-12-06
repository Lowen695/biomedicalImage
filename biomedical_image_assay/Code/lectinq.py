import cv2 as cv
import numpy as np

img = cv.imread('../../opencv-course/Resources/lectin.jpg')
cv.imshow('Originfig',img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur = cv.medianBlur(gray,7,cv.BORDER_ISOLATED)
threshold, thresh = cv.threshold(blur,5,255,0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img,contours,-1,(0,0,255),thickness=1)
print(f'There are {len(contours)} blots can be detected')

for i,contour in enumerate(contours):
    blank = np.zeros(gray.shape, dtype='uint8')
    area = cv.contourArea(contours[i])
    x,y,w,h = cv.boundingRect(contour)
    cv.putText(img, f'{i}', (x, y), cv.FONT_HERSHEY_COMPLEX_SMALL,
               fontScale=0.5, color=(0, 255, 0), thickness=1)
    mask = cv.drawContours(blank, contours[i:i+1], -1, (255, 255, 255), -1)
    meanIntensity = cv.mean(gray,mask=mask)
    print(f'Dot {i} with area {area} and mean intensity {int(meanIntensity[0])}')

cv.imshow('figWithBlotsDetected',img)

cv.waitKey(0)