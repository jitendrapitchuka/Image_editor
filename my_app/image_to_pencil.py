
import numpy as np
import cv2

img = "pubg.jpeg"
img_read = cv2.imread(img)
cv2.imshow('img_read',img_read)
cv2.waitKey(0)

def rgb2gray(rgb):
	#Y= 0.299 R + 0.587 G + 0.114 B
	return np.dot(rgb[..., :3], [0.2989, 0.5870, .1140])

def dodge(front, back):
    final_sketch = front*255/(255-back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    return final_sketch.astype('uint8')

def click_event1(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        text="hello this a text1"
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (0, 0, 0)
        fontScale = 1
        
        cv2.putText(r,text,(x,y),font,fontScale,color)
        cv2.imshow('image',r)


gray = rgb2gray(img_read)
i = 255-gray

# to convert into a blur image

blur = cv2.GaussianBlur(i, (29,29),0)


r = dodge(blur, gray)
print(r)
print(r.shape)


cv2.imshow('image',r)
cv2.setMouseCallback('image',click_event1)
cv2.waitKey(0)
cv2.destroyAllWindows()
