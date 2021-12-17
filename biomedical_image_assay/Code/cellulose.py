import cv2 as cv
import numpy as np
from skimage.segmentation import clear_border
from skimage import measure
import matplotlib.pyplot as plt
import pandas as pd

imge = cv.imread('../Resources/elisa.png')
img = cv.cvtColor(imge,cv.COLOR_BGR2GRAY)
cv.imshow('Redchannel',img)


threshold, thresh = cv.threshold(img,200,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
# cv.imshow('Originfig2',thresh)

# remove noise
kernel = np.ones((2,2),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_CLOSE,kernel, iterations = 1)
closing = cv.morphologyEx(opening,cv.MORPH_ERODE,kernel, iterations = 2)

# cv.imshow('withoutNoice',closing)

# remove cells on the border
clearBorder = clear_border(closing)
clearBorder2 = cv.morphologyEx(clearBorder,cv.MORPH_OPEN,kernel, iterations = 1)
cv.imshow('borderClear',clearBorder2)

sure_bg = cv.dilate(clearBorder2,kernel,iterations=8)
cv.imshow('sureBG',sure_bg)
dist_transform = cv.distanceTransform(clearBorder2,cv.DIST_L2,5)
ret,sure_fg = cv.threshold(dist_transform,0.3*dist_transform.max(),255,0)
cv.imshow('sureFG',sure_fg)
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg,sure_fg)
cv.imshow('Unknown',unknown)
ret, markers = cv.connectedComponents(sure_fg)
markers = markers + 5
markers[unknown==255] = 0
markers = cv.watershed(imge,markers)
imge[markers==-1] = [255,0,0]

markers = markers.astype(np.uint8)

contours,hierarchy = cv.findContours(markers,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
cv.drawContours(imge,contours,-1,(0,255,0),thickness=3)


plt.imshow(imge)
plt.show()

props = measure.regionprops_table(markers, imge,properties=['label',
                                      'area', 'mean_intensity'])

df = pd.DataFrame(props)
df.to_csv('Result_elisa.csv')


cv.waitKey(0)