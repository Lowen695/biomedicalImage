import cv2 as cv


cv.namedWindow('Gray')

def binarization(th):
    img = cv.imread('../Resources/domi2.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray[gray<th]=0
    gray[gray>th]=255
    value = str(cv.getTrackbarPos('bar1','Gray'))
    cv.putText(gray,f'Current threshold: {value}',(10,100),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),thickness=2)
    cv.imshow('Gray',gray)


cv.createTrackbar('bar1', 'Gray', 1, 200,binarization)

binarization(0)
cv.waitKey()



