import cv2 as cv
import numpy as np

img =  cv.imread('../../opencv-course/Resources/Photos/cat.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_WRAP)
cv.imshow('Blue', blur)

edge = cv.Canny(img,200,200)
cv.imshow('Edge', edge)

resized = cv.resize(img,(100,200))
cv.imshow('Resized', resized)

cropped = img[100:400,100:1200]
cv.imshow('Cropped', cropped)

flip = cv.flip(img,0)
cv.imshow('Flipped', flip)

cv.waitKey(0)