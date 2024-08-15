from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Users

def index(request):
    users = Users.objects.all()
    return render(request,'users.html',{'users':users})

def addNew(request):
    return render(request,'add.html')

def insertUser(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    Users.objects.create(username=username,email=email,password=password)
    return redirect('/')

def deleteUser(request,id):
    user = Users.objects.get(id=id)
    user.delete()
    users = Users.objects.all()
    return redirect('/')

def editUser(request,id):
    users = Users.objects.get(id=id)
    return render(request,'editUser.html',{'users':users})

def updateUser(request,id):
    id = request.POST['id']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    Users.objects.filter(id=id).update(username=username,email=email,password=password)
    return redirect('/')