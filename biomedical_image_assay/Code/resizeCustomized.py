import cv2 as cv
import numpy as np


def custom_resize(image, scale = 2):
    old_width = image.shape[0]
    old_height = image.shape[1]

    new_width = image.shape[0]*scale
    new_height = image.shape[1]*scale

    x_scale = new_width / (old_width - 1)
    y_scale = new_height / (old_height - 1)

    new_image = np.zeros(shape=(new_width, new_height, image.shape[-1]), dtype=np.uint8)

    for new_x in range(new_width):
        for new_y in range(new_height):
            new_image[new_x, new_y] = image[round(new_x / x_scale), round(new_y / y_scale)]

    return new_image

img = cv.imread('../Resources/domi3.jpg')
cv.imshow('Origin',img)
out = custom_resize(img,scale = 3)
cv.imshow('Resized',out)
cv.waitKey()