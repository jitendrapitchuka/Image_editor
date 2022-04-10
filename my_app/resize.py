import cv2
import numpy as np
def size(image,file1_width,file1_height):
    img=cv2.imread(image)
    width=int(file1_width)
    height=int(file1_height)
    img=cv2.resize(img,(width,height),)
    cv2.imwrite('/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/static/final.png',img)
    return "/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/static/final.png"