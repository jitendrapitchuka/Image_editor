from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from my_app.meme import meme_gen
from my_app.histogram import histogrameq
from my_app.histogramrgb import his
from my_app.resize import size
from my_app.filter import filter_conv
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
        
        myfile=file_paths[0]
        if os.path.isfile(myfile):
            os.remove(myfile)
            os.remove(file_paths[1])
                    
                    
            
        return render(request,'output.html')
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
        
        myfile=file_paths[0]
        if os.path.isfile(myfile):
            os.remove(myfile)
        temp=1 
        return render(request, 'output.html',{'temp':temp})        
                    
              
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
        
        myfile=file_paths[0]
        if os.path.isfile(myfile):
            os.remove(myfile)
        temp=1;            
        return render(request,'output.html',{'temp':temp})
         
                    
               
          
    return render(request,'his.html')


def resize(request):
    if(request.method=='POST'):
       
        file1_width=request.POST.get('file1_width')
        file1_height=request.POST.get('file1_height')
        fs = FileSystemStorage()
       
        file_paths = []
        
        for file_name in request.FILES:
            upload_file = request.FILES[file_name]
            extension = os.path.splitext(upload_file.name)[1]
            file_path = os.path.join(settings.MEDIA_ROOT_URL, file_name + extension)
            file_paths.append(file_path)
            filename = fs.save(file_path, request.FILES[file_name])
        img_path= size(*file_paths,file1_width,file1_height)
        myfile=file_paths[0]
        if os.path.isfile(myfile):
            os.remove(myfile)
        # path='/home/jitendra/learning/github_repos/django_projects/Image_editor/my_app/static/final.png'
        # image_path = os.path.basename(path)
       
        return render(request, 'output.html')
        

    return render(request, 'resize.html')

def filters(request):
    if(request.method=='POST'):
       
        colour1_input=request.POST.get('colour1_input')
        fs = FileSystemStorage()
       
        file_paths = []
        
        for file_name in request.FILES:
            upload_file = request.FILES[file_name]
            extension = os.path.splitext(upload_file.name)[1]
            file_path = os.path.join(settings.MEDIA_ROOT_URL, file_name + extension)
            file_paths.append(file_path)
            filename = fs.save(file_path, request.FILES[file_name])
        if(colour1_input=='gray'):
            img_path= filter_conv(*file_paths,colour1_input)
        if(colour1_input=='ycrcb'):
            img_path= filter_conv(*file_paths,colour1_input)
        myfile=file_paths[0]
        if os.path.isfile(myfile):
            os.remove(myfile)
        temp=1
        return render(request, 'output.html',{'temp':temp})
        

    return render(request, 'filter.html')

  

