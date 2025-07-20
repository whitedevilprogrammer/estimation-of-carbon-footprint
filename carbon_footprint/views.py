from django.http import HttpResponse
from .models import register
from django.shortcuts import render, redirect
# Create your views here.

def registerpage(request):
    if request.method == 'POST':
        getname = request.POST.get('name')
        getaddress = request.POST.get('address')
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        users = register()
        users.Name = getname
        users.Address = getaddress
        users.Username = getusername
        users.Password = getpassword
        users.save()

    return render(request,'usersignup.html')

def userlog(request):
    if request.method == 'POST':
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        try:
            register.objects.get(Username=getusername,Password=getpassword)
            return redirect('/mainpage')
        except:
            return HttpResponse('Invalid User')
    return render(request,'userlogin.html')

def mainpage(request):
    return render(request,'mainpage.html')

def adminlog(request):
    if request.method == 'POST':
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        if getusername == 'admin' and getpassword == 'admin':
            return redirect('/adminloginoptions')
        else:
            return HttpResponse('Invalid')
    return render(request,'adminlogin.html')

def adminlogoptions(request):
    return render(request,'adminloginoptions.html')

def pending(request):
    details = register.objects.filter(Status=False)
    return render(request,'pendinglist.html',{'value': details})

def approved(request):
    details = register.objects.filter(Status=True)
    return render(request,'approvedlist.html',{'value': details})

def approve(request,id):
    data = register.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/pending')

def operations(request):
    details = register.objects.all()
    return render(request,'operations.html',{"value": details})

def edit(request,id):
    data = register.objects.all()
    users = register.objects.get(id=id)
    if request.method == 'POST':
        getaddress = request.POST.get('address')
        getpassword = request.POST.get('password')
        users.Address = getaddress
        users.Password = getpassword
        users.save()
        return redirect('/operations')
    return render(request,'operations.html',{'value':data,'user_data': users})

def delete(request,id):
    data = register.objects.filter(id=id).delete()
    return redirect('/operations')




