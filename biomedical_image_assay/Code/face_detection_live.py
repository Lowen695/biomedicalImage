import cv2 as cv
import os

video = cv.VideoCapture(0)
faceDetector = cv.CascadeClassifier('haar_face.xml')

while True:
    isTrue, img = video.read()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faceDetected = faceDetector.detectMultiScale(gray, 1.1, 3)
    for x,y,w,h in faceDetected:
        cv.putText(img,'Fahui',(x+5,y-10),cv.FONT_HERSHEY_COMPLEX_SMALL,fontScale=2,color=(0,255,0),thickness=1)
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv.imshow('Facedetected', img)

    if cv.waitKey(10) & 0xFF == ord('c'):
        os.system("say 'bye bye, fahui Liu'")
        break

video.release()
cv.destroyAllWindows()