import cv2
import numpy as np
import os
def meme(image1,image2):
    img1=cv2.imread(image1)
    img2=cv2.imread(image2)
    width=500
    height=300
    img1=cv2.resize(img1,(width,height))
    img2=cv2.resize(img2,(width,height))

    adding=np.concatenate((img1,img2),axis=0)

    def click_event1(event,x,y,flags,param):
        if event==cv2.EVENT_LBUTTONDOWN:
            text="hello this a text1"
            font = cv2.FONT_HERSHEY_SIMPLEX
            color = (255, 255, 255)
            fontScale = 1
            
            cv2.putText(adding,text,(x,y),font,fontScale,color)
            cv2.imshow('image',adding)


        if event==cv2.EVENT_RBUTTONDOWN:
            text="hello this a text2"
            font = cv2.FONT_HERSHEY_SIMPLEX
            color = (255, 255, 255)
            fontScale = 1
            cv2.putText(adding,text,(x,y),font,fontScale,color)
            cv2.imshow('image',adding)
            
        cv2.imshow('image',adding)
        cv2.setMouseCallback('image',click_event1)


        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite('/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/media/final.png',dst)
    return "/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/media/final.png"

    