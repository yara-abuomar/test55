from django.shortcuts import render ,redirect
from.models import *
from django.contrib import messages

def method(request):
    return render(request ,'index.html')
def method1(request):
    errors=Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request ,value)
        return redirect('/')
    else:
        show1=Show.objects.create(title=request.POST['title1'],network=request.POST['net'],release_date=request.POST['rele'],desc=request.POST['desc1'])
        return redirect('/shows/'+str(show1.id))

def method3(request,id):
    context={
        'oneshow':Show.objects.get(id=int(id))
    }
    return render(request ,'details.html',context)
def delet(request,num):
    show1=Show.objects.get(id=int(num))
    show1.delete()
    return redirect('/')
def method4(request):
    context={
        'allshow':Show.objects.all()
    }
    return render(request ,'all.html',context)

def method5(request,id1):
    context={
        'edit':Show.objects.get(id=int(id1))
    }
    return render(request ,'edit.html',context)
def method6(request,num1):
    errors=Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request ,value)
        return redirect('/')
    else:
        show1=Show.objects.get(id=int(num1))
        show1.title=request.POST['title1']
        show1.network=request.POST['net']
        show1.release_date=request.POST['rele']
        show1.desc=request.POST['desc1']
        show1.save()
        return redirect('/shows')


        











# Create your views here.
