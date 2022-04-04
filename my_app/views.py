from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from my_app.meme import meme_gen
from my_app.histogram import histogrameq
from my_app.histogramrgb import his
import os
# Create your views here.



def meme(request):
    
    if(request.method=='POST'):
        print(request.POST)
        file1_input=request.POST.get('file1_input')
        file2_input=request.POST.get('file2_input')
        colour1_input=request.POST.get('colour1_input')
        
        colour2_input=request.POST.get('colour2_input')
        
        fs = FileSystemStorage()
       
        file_paths = []
        print(request.FILES)
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

        if(colour1_input=="black" and colour2_input=="black"):
            img_path= meme_gen(*file_paths,file1_input,file2_input,colour1_input,colour2_input)
        if(colour1_input=="white" and colour2_input=="white"):
            img_path= meme_gen(*file_paths,file1_input,file2_input,colour1_input,colour2_input)
        if(colour1_input=="white" and colour2_input=="black"):
            img_path= meme_gen(*file_paths,file1_input,file2_input,colour1_input,colour2_input)
        if(colour1_input=="black" and colour2_input=="white"):
            img_path= meme_gen(*file_paths,file1_input,file2_input,colour1_input,colour2_input)
       
        
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


def histogram(request):
    if(request.method=='POST'):
       
        
        fs = FileSystemStorage()
       
        file_paths = []
        print(request.FILES)
        for file_name in request.FILES:
            upload_file = request.FILES[file_name]
            extension = os.path.splitext(upload_file.name)[1]
            file_path = os.path.join(settings.MEDIA_ROOT_URL, file_name + extension)
            file_paths.append(file_path)
            filename = fs.save(file_path, request.FILES[file_name])
        img_path= histogrameq(*file_paths)
        try:
            with open(img_path, "rb") as f:
                myfile=file_paths[0]
                if os.path.isfile(myfile):
                    os.remove(myfile)
                    
                    
                    
                return HttpResponse(f.read(), content_type="image/jpeg")
            #return render(request,'output.html',{'img_path':img_path})
        except IOError:
            return render(request,'histogram.html')
    return render(request,'histogram.html')

def histrgb(request):
    if(request.method=='POST'):
       
        
        fs = FileSystemStorage()
       
        file_paths = []
        print(request.FILES)
        for file_name in request.FILES:
            upload_file = request.FILES[file_name]
            extension = os.path.splitext(upload_file.name)[1]
            file_path = os.path.join(settings.MEDIA_ROOT_URL, file_name + extension)
            file_paths.append(file_path)
            filename = fs.save(file_path, request.FILES[file_name])
        img_path= his(*file_paths)
        try:
            with open(img_path, "rb") as f:
                myfile=file_paths[0]
                if os.path.isfile(myfile):
                    os.remove(myfile)
                    
                    
                    
                return HttpResponse(f.read(), content_type="image/jpeg")
           
        except IOError:
            return render(request,'his.html')
    return render(request,'his.html')

