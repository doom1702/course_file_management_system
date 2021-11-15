from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    
    return render(request,"home.html")

@login_required
def vision(request):
    if request.method=="POST":
        form = MyFileUploaded(request.POST,request.FILES)
        
        if form.is_valid():
            files = File(user=request.user,file_name=request.POST['file_name'],file_link=request.FILES['file_link'])
            files.save()
        messages.success(request,f'File Uploaded from {request.user.username} Successfully!')
    else:
        form = MyFileUploaded()
    files = File.objects.filter(user=request.user)
    context = {'files':files,'form':form}
    return render(request,'vision.html',context)

def delete_files(request,pk=None):
    File.objects.get(id=pk).delete()
    return redirect('vision')

@login_required
def depart(request):
    if request.method=="POST":
        form = Dep_File_Upload(request.POST,request.FILES)
        
        if form.is_valid():
            files = Dep_File(user=request.user,file_name=request.POST['file_name'],file_link=request.FILES['file_link'])
            files.save()
        messages.success(request,f'File Uploaded from {request.user.username} Successfully!')
    else:
        form = Dep_File_Upload()
    files = Dep_File.objects.filter(user=request.user)
    context = {'files':files,'form':form}
    return render(request,'depart.html',context)

@login_required
def ict(request):
    if request.method=="POST":
        form = ICT_File_Upload(request.POST,request.FILES)
        
        if form.is_valid():
            files = Ict_File(user=request.user,file_name=request.POST['file_name'],file_link=request.FILES['file_link'])
            files.save()
        messages.success(request,f'File Uploaded from {request.user.username} Successfully!')
    else:
        form = ICT_File_Upload()
    files = Ict_File.objects.filter(user=request.user)
    context = {'files':files,'form':form}
    return render(request,'ict.html',context)

@login_required
def qb(request):
    if request.method=="POST":
        form = Qb_File_Upload(request.POST,request.FILES)
        
        if form.is_valid():
            files = Qb_File(user=request.user,file_name=request.POST['file_name'],file_link=request.FILES['file_link'])
            files.save()
        messages.success(request,f'File Uploaded from {request.user.username} Successfully!')
    else:
        form = Qb_File_Upload()
    files = Qb_File.objects.filter(user=request.user)
    context = {'files':files,'form':form}
    return render(request,'qb.html',context)

@login_required
def rubrics(request):
    if request.method=="POST":
        form = Rubrics_File_Upload(request.POST,request.FILES)
        
        if form.is_valid():
            files = Rubrics_File(user=request.user,file_name=request.POST['file_name'],file_link=request.FILES['file_link'])
            files.save()
        messages.success(request,f'File Uploaded from {request.user.username} Successfully!')
    else:
        form = Rubrics_File_Upload()
    files = Rubrics_File.objects.filter(user=request.user)
    context = {'files':files,'form':form}
    return render(request,'rubrics.html',context)

@login_required
def syllab(request):
    if request.method=="POST":
        form = Syllab_File_Upload(request.POST,request.FILES)
        
        if form.is_valid():
            files = Sylab_File(user=request.user,file_name=request.POST['file_name'],file_link=request.FILES['file_link'])
            files.save()
        messages.success(request,f'File Uploaded from {request.user.username} Successfully!')
    else:
        form = Syllab_File_Upload()
    files = Sylab_File.objects.filter(user=request.user)
    context = {'files':files,'form':form}
    return render(request,'syllab.html',context)

@login_required
def uni_exam(request):
    if request.method=="POST":
        form = Uni_Exam_File_Upload(request.POST,request.FILES)
        
        if form.is_valid():
            files = Uni_Exam_File(user=request.user,file_name=request.POST['file_name'],file_link=request.FILES['file_link'])
            files.save()
        messages.success(request,f'File Uploaded from {request.user.username} Successfully!')
    else:
        form = Uni_Exam_File_Upload()
    files = Uni_Exam_File.objects.filter(user=request.user)
    context = {'files':files,'form':form}
    return render(request,'uni_exam.html',context)

def delete_dep(request,pk=None):
    Dep_File.objects.get(id=pk).delete()
    return redirect('depart')

def delete_rubrics(request,pk=None):
    Rubrics_File.objects.get(id=pk).delete()
    return redirect('rubrics')

def delete_syllab(request,pk=None):
    Sylab_File.objects.get(id=pk).delete()
    return redirect('syllab')

def delete_ict(request,pk=None):
    Ict_File.objects.get(id=pk).delete()
    return redirect('ict')

def delete_uni_exam(request,pk=None):
    Uni_Exam_File.objects.get(id=pk).delete()
    return redirect('uni_exam')

def delete_qb(request,pk=None):
    Qb_File.objects.get(id=pk).delete()
    return redirect('qb')

def admin(request):
    return redirect('admin/login/?next=/admin/')
# def profile(request):
#     return render(request,'profile.html')