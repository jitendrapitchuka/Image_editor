import cv2
import os
def filter_conv(image,colour1_input):
    img = cv2.imread(image)

    if(colour1_input=='gray'):
        imag = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if(colour1_input=='ycrcb'):
         imag=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)

   



    cv2.imwrite('/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/static/input.png',img)
    cv2.imwrite('/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/static/final.png',imag)
    return "/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/static/final.png"
