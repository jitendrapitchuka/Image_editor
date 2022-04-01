import numpy as np
import cv2

def histogrameq(image):


    img = cv2.imread(image)

    #To display image before equalization
    

    ycrcb=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)


    channels=cv2.split(ycrcb)
    a = np.zeros((256,),dtype=np.float16)

    height,width=channels[0].shape
    img1=channels[0]
    
    #finding histogram
    for i in range(width):
        for j in range(height):
            g = channels[0][j,i]
        
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
            g = channels[0][j,i]
            channels[0][j,i]= b[g]
    # channels[0]=img1
    print(img1)
    ycrcb=cv2.merge(channels)

    img2=cv2.cvtColor(ycrcb,cv2.COLOR_YCR_CB2BGR)
    






    cv2.imwrite('/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/media/final.png',img2)
    return "/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/media/final.png"
