# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm
from .models import *
import os,re,csv
import settings

@login_required(login_url='/accounts/login/')
def myaccount(request):
    if request.method=='POST':
        form=FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            request.FILES['files'].name = request.FILES['files'].name +'_'+ str(request.user.id)
            
            FileUploadForm(request.POST,request.FILES).save()
            
            csvfile=request.FILES['files']
            count=0
            for row in csv.reader(csvfile):
                if not count==0:
                    save_obj=SaveCSV(user=request.user,title=request.FILES['files'].name,
                                     name=row[0],address=row[1],phone=int(row[2]),city=row[3])
                    save_obj.save()
                count=+1        
    else:
        form=FileUploadForm()
        
                
    host=request.META['HTTP_HOST']
    country=request.user.get_profile().country
    
    return render_to_response('myaccount.html', locals(),context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def list_files(request):
    list_files=os.listdir(settings.PROJECT_DIR+'/media/files')
    pattren=re.compile("(.*)_"+str(request.user.id)+"(_(.*))?")
    user_files=[]
    for file_name in list_files:
        if pattren.match(file_name):
            file_name=file_name[:-2]
            user_files.append(file_name)
    no_uploads=len(user_files)        
    return render_to_response('list_files.html', locals(),context_instance=RequestContext(request))        
    
@login_required(login_url='/accounts/login/')
def csv_data(request):
    
    
    csv_data_dict=SaveCSV.objects.filter(user=request.user).values('title','name','address','phone','city')
    
    return render_to_response('csv_data.html',locals(),context_instance=RequestContext(request))
    
        
    
