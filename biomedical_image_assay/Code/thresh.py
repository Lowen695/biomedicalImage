import cv2 as cv

img =  cv.imread('../../opencv-course/Resources/Photos/cats.jpg')
img2 = cv.imread('../../opencv-course/Resources/Photos/cat.jpg')
cv.imshow('Cats',img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(gray,200,255,cv.THRESH_BINARY)
cv.imshow('Simple thresh',thresh)
print(threshold)

mask = cv.bitwise_and(img, img,mask=thresh)
cv.imshow('Masked',mask)

cv.waitKey(0)


