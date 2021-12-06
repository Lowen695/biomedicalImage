import cv2 as cv
from faceRecgnizer import person

faceDetector = cv.CascadeClassifier('haar_face.xml')
faceRecognizer = cv.face.LBPHFaceRecognizer_create()
faceRecognizer.read('trainedFaceRecognizer.yml')
p= person()

img = cv.imread(r'/Faces/val/madonna/4.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faceDetected = faceDetector.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=3)

for x,y,w,h in faceDetected:
    faceDetectedMarked = gray[y:y+h,x:x+w]
    label, confidence = faceRecognizer.predict(faceDetectedMarked)

    print(f'Label = {p[label]} with a confidence of {confidence}')
    cv.putText(img,str(p[label]),(30,30),cv.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,255,0),thickness=2)
    cv.putText(img, f'With confidence {int(confidence)}%', (30, 50),
               cv.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.6, color=(0, 255, 0), thickness=1)
    cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)

cv.imshow('RecognitionResults',img)
cv.waitKey(0)
