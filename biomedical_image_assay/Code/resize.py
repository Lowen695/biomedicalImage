import cv2 as cv


video = cv.VideoCapture(0)


def resize_frame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = video.read()
    cv.imshow('Video',frame)

    frame_resized = resize_frame(frame)
    cv.imshow('Video_resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('c'):
        break

video.release()
cv.destroyAllWindows()