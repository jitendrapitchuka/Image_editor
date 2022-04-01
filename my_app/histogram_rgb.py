import cv2
import os

img = cv2.imread("nature.jpg")

cv2.imshow('img', img)
cv2.waitKey(0)

ycrcb=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
channels=cv2.split(ycrcb)

cv2.equalizeHist(channels[0],channels[0])
ycrcb=cv2.merge(channels)
img2=cv2.cvtColor(ycrcb,cv2.COLOR_YCR_CB2BGR,img)
    




cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
