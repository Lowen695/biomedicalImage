# Lowen python 练习
# 编写时间 03/12/2021 12:04
import cv2 as cv
import numpy as np

# img = cv.imread('elisa.png')
# print(type(img))

a = np.arange(0,30,2)
b=a.reshape(3,5)
c = np.mean(b[1:2,0:3])
print(b,b[1:2,0:3],c)
