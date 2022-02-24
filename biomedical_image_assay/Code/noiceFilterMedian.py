import cv2 as cv
import numpy as np

def gaussian_filter(img, k_size = 3):
    if len(img.shape) == 3:
        h,w,c = img.shape
    else:
        img = np.expand_dims(img,axis=-1)
        h, w, c = img.shape

    pad = k_size//2
    out = np.zeros((h+pad*2, w+pad*2,c),dtype=np.float64)
    out[pad:pad+h,pad:pad+w]=img.copy().astype(np.float64)

    tmp = out.copy()
    for y in range(h):
        for x in range(w):
            for c in range(3):
                out[pad + y, pad + x, c] = np.median(tmp[y:y + k_size, x:x + k_size, c])

    out = out[pad:pad + h, pad:pad + w].astype(np.uint8)
    print(range(h))
    return out

img = cv.imread('../Resources/cells.jpeg')
cv.imshow('Original',img)
out = gaussian_filter(img)
cv.imshow('Result',out)
cv.waitKey()

