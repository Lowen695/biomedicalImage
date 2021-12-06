import cv2 as cv

img = cv.imread('../../opencv-course/Resources/Photos/cat.jpg')
cv.imshow('cat', img)
cv.waitKey(0)
cv.destroyAllWindows()


# video = cv.VideoCapture(0)
#
# while True:
#     isTrue, frame = video.read()
#     cv.imshow('Video',frame)
#
#     if cv.waitKey(20) & 0xFF == ord('c'):
#         break
#
# video.release()
# cv.destroyAllWindows()