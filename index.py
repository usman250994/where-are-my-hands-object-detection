import cv2
import numpy as np
import imutils

frame = cv2.imread('hands-image.png')
converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

cv2.imshow('read-frame', frame)
cv2.imshow('hsv-converted-frame', converted)

lower_bound = np.array([0, 100, 70])
upper_bound = np.array([20, 150, 200])
skinMask = cv2.inRange(converted, lower_bound, upper_bound)
cv2.imshow('skin_mask_frame', skinMask)

cv2.waitKey(0)
