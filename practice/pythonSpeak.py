# Lowen python 练习
# 编写时间 03/12/2021 12:04
import cv2 as cv
import numpy as np
import pyttsx3

# img = cv.imread('elisa.png')
# print(type(img))

engine = pyttsx3.init()
engine.setProperty('rate',200)
# voices = engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)
engine.say('we will we will fuck you')
engine.runAndWait()
engine.stop()

