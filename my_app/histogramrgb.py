import cv2
import os
def his(image):
    image = cv2.imread(image)

    
    ycrcb=cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB)
    channels=cv2.split(ycrcb)

    img=cv2.equalizeHist(channels[0],channels[0])
    ycrcb=cv2.merge(channels)
    img2=cv2.cvtColor(ycrcb,cv2.COLOR_YCR_CB2BGR,img)
    cv2.imwrite('/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/static/input.png',image)

    cv2.imwrite('/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/static/final.png',img2)
    return "/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/static/final.png"
    





