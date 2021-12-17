import cv2 as cv
import numpy as np

def average_pooling(img,G=20):
    out = img.copy()

    h,w,c = out.shape
    nh = int(h/G)
    nw = int(w/G)
    for y in range(nh):
        for x in range(nw):
            for c in range(3):
                out[G*y:G*(y+1),G*x:G*(x+1),c] = np.mean(out[G*y:G*(y+1),G*x:G*(x+1),c])
    print(nh,nw,c, out.shape)
    return out

img = cv.imread('../Resources/domi2.jpg')
out = average_pooling(img)
cv.imwrite("out.jpg", out)
cv.imshow('Result',out)
cv.waitKey(0)