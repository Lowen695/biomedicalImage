import os
import cv2 as cv
import numpy as np

def person():
    p = []
    for i in os.listdir(r'/Faces/train'):
        p.append(i)
    return p
p= person()
DIR = r'/Faces/train'
faceDetector = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []
def creat_train():
    for person in p:
        path = os.path.join(DIR, person)
        label = p.index(person)
        for img_first_path in os.listdir(path):
            img_path = os.path.join(path,img_first_path)
            img = cv.imread(img_path)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            faceDetected = faceDetector.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)
            for x,y,w,h in faceDetected:
                faceInsterested = gray[y:y+h,x:x+w]
                features.append(faceInsterested)
                labels.append(label)

creat_train()

featuresFormated = np.array(features,dtype='object')
labelsFormated = np.array(labels)

faceRecognizer = cv.face.LBPHFaceRecognizer_create()
faceRecognizer.train(featuresFormated,labelsFormated)
faceRecognizer.save('trainedFaceRecognizer.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
print('Training has been done')
