
import cv2 as cv
import numpy as np
import datetime

def bgr2gray(img):
    b = img[:,:,0].copy()
    g = img[:,:,1].copy()
    r = img[:,:,2].copy()

    out = 0.2126*r + 0.7152*g + 0.0722*b
    return out

def max_min_filter(gray,k_size = 2):
    H, W = gray.shape
    pad = k_size//2
    out = np.zeros((H+pad*2,W+pad*2),dtype=np.uint8)
    out[pad:pad+H,pad:pad+W] = gray.copy()

    temp = out.copy()

    for y in range(H):
        for x in range(W):
            out[pad + y, pad+x] = np.max((temp[y: y + k_size, x: x + k_size]) - \
                                  np.min(temp[y: y + k_size, x: x + k_size]))

    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out

img = cv.imread('biomedical_image_assay/Resources/domi3.jpg')
gray = bgr2gray(img)
out = max_min_filter(gray,k_size=6)
cv.imshow('Result',out)
cv.waitKey()