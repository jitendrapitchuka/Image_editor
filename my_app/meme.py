import cv2
import numpy as np
import os
def meme_gen(image1,image2):
    
    img1=cv2.imread(image1)
    img2=cv2.imread(image2)
    width=500
    height=300
    img1=cv2.resize(img1,(width,height))
    text="hello this a text1"
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 255, 255)
    fontScale = 1
    
    cv2.putText(img1,text,(50,50),font,fontScale,color,2)
    img2=cv2.resize(img2,(width,height))
    text="hello this a text2"
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 255, 255)
    fontScale = 1
    
    cv2.putText(img2,text,(50,50),font,fontScale,color,2)
    adding=np.concatenate((img1,img2),axis=0)

    
    
    
    print("from meme_____")
    # cv2.imshow('image',adding)
    

    
    # cv2.waitKey(10)
    # cv2.destroyAllWindows()
    cv2.imwrite('/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/media/final.png',adding)
    return "/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/media/final.png"

    