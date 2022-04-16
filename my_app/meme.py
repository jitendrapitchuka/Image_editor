import cv2
import numpy as np
import os
def meme_gen(image1,image2,file1_input,file2_input,colour1_input,colour2_input):
    
    img1=cv2.imread(image1)
    img2=cv2.imread(image2)
    width=500
    height=300
    img1=cv2.resize(img1,(width,height))
    text=file1_input
    font = cv2.FONT_HERSHEY_SIMPLEX
    print(colour1_input)
    print(colour2_input)
    if(colour1_input=="black"):
        color1 = (0, 0, 0)
    if(colour1_input=="white"):
        color1 = (255, 255, 255)
    fontScale = 1
    
    cv2.putText(img1,text,(50,50),font,fontScale,color1,2)
    img2=cv2.resize(img2,(width,height))
    text=file2_input
    font = cv2.FONT_HERSHEY_SIMPLEX
    if(colour2_input=="black"):
        color2 = (0, 0, 0)
    if(colour2_input=="white"):
        color2 = (255, 255, 255)
    
    
    fontScale = 1
    
    cv2.putText(img2,text,(50,50),font,fontScale,color2,2)
    adding=np.concatenate((img1,img2),axis=0)

    
    
    
    
    # cv2.imshow('image',adding)
    

    
    # cv2.waitKey(10)
    # cv2.destroyAllWindows()
    
    cv2.imwrite('/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/static/final.png',adding)
    return "/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/static/final.png"

    