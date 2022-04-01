import numpy as np
import cv2

def histogrameq(image):
    img = cv2.imread(image,0)
    

   


    a = np.zeros((256,),dtype=np.float16)

    height,width=img.shape

    #finding histogram
    for i in range(width):
        for j in range(height):
            g = img[j,i]
        
            a[g] = a[g]+1
            

   


    #performing histogram equalization
    tmp = 1.0/(height*width)
    b = np.zeros((256,),dtype=np.float16)

    for i in range(256):
        for j in range(i+1):
            b[i] += a[j] * tmp;
        b[i] = round(b[i] * 255);

    # b now contains the equalized histogram
    b=b.astype(np.uint8)

    


    for i in range(width):
        for j in range(height):
            g = img[j,i]
            img[j,i]= b[g]


    cv2.imwrite('/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/media/final.png',img)
    return "/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/media/final.png"
