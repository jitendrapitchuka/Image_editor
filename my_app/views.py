from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from my_app.meme import meme
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

          
        img_path= meme(file_paths[0],file_paths[1])
        try:
            with open(img_path, "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError:
            return render(request,'meme.html')
    return render(request,'meme.html')

def index(request):
     return render(request,'index.html')