from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from my_app.meme import meme_gen
import os
# Create your views here.




def meme(request):
    
    if(request.method=='POST'):
        print(request.POST)
        
        fs = FileSystemStorage()
       
        file_paths = []
        for file_name in request.FILES:
            
            upload_file = request.FILES[file_name]
            print(upload_file)
            extension = os.path.splitext(upload_file.name)[1]
            print(extension)
            file_path = os.path.join(settings.MEDIA_ROOT_URL, file_name + extension)
            print(file_path)
            file_paths.append(file_path)
            print(file_paths)
            filename = fs.save(file_path, request.FILES[file_name])

          
        img_path= meme_gen(*file_paths)
        print(img_path)
        try:
            with open(img_path, "rb") as f:
                myfile=file_paths[0]
                if os.path.isfile(myfile):
                    os.remove(myfile)
                    os.remove(file_paths[1])
                    
                    
                return HttpResponse(f.read(), content_type="image/jpeg")
            #return render(request,'output.html',{'img_path':img_path})
        except IOError:
            return render(request,'meme.html')
    return render(request,'meme.html')

def index(request):
     return render(request,'index.html')

# def output_meme(request):
#     def click_event1(event,x,y,flags,param):
#         if event==cv2.EVENT_LBUTTONDOWN:
#             text="hello this a text1"
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             color = (255, 255, 255)
#             fontScale = 1
            
#             cv2.putText(adding,text,(x,y),font,fontScale,color)
#             cv2.imshow('image',adding)


#         if event==cv2.EVENT_RBUTTONDOWN:
#             text="hello this a text2"
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             color = (255, 255, 255)
#             fontScale = 1
#             cv2.putText(adding,text,(x,y),font,fontScale,color)
#             cv2.imshow('image',adding)
#     cv2.setMouseCallback('image',click_event1)
#     return render(request,'ouput_meme.html')