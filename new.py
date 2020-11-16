import cv2
from blockmatching import *
from numpy import  hstack
cap = cv2.VideoCapture('casa_480.mp4')
started = False
old_frame = None
background = None
# Learning rate
alpha = 0.01

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if started is False:
            background = BackgroundSubtractor(alpha, frame)
            foreground = background.foreground(frame)
            started = True
        else:
            foreground = background.foreground(frame)
            img = hstac(background.background, foreground)
            cv2.imshow('Background x Foreground', img)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    else:
         break

cap.release()