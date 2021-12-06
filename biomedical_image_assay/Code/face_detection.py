import cv2 as cv

img = cv.imread('../../opencv-course/Resources/Photos/group 1.jpg')
cv.imshow('Lady',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray_lady',gray)

faceDetector = cv.CascadeClassifier('haar_face.xml')
faceDetected = faceDetector.detectMultiScale(gray, 1.1, 1)
print(f'Number of face found = {len(faceDetected)}')
print(faceDetected[1])

i=0
for x,y,w,h in faceDetected:
    i+=1
    cv.putText(img,f'{i}',(x+5,y+15),cv.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(100,255,255),thickness=1)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
cv.imshow('Facedetected',img)
cv.waitKey(0)