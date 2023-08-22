from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def loginPage(request):
   return render(request, 'login.html')

# def login(request):
#     if request.method=='POST':
#         username= request.POST ['uname']
#         password= request.POST ['psw']
#         print(username)
#         print(password)
   
        
#     if username == username and password == password :
#         return render(request,'detail.html',{'name': username ,'password': password})
#     else:
#         return render(request,'logim.hmtl')

# def kk (request) : 
#      return render(request, 'kk.html')
    
    
def home (request) :
        event = Event.objects.all()

        return render(request,'index.html',{'myevent':event})


# def mm(request) :
#      return render(request,'mm.html' )


def registerPage(request) :
     
     return render(request,'registration.html')

def login(request) :
    if request.method == 'POST':
        username =request.POST.get('uname')
        password = request.POST.get('psw')
        user = auth.authenticate(username=username, password = password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'logged in succesfull')
            return redirect('home')
        else:
            messages.error(request,'wrong username or password')
            return redirect('loginpage')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password == password2:
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already used')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, password=password)
                user.save()
                messages.success(request, 'Signup Successfully')
                return redirect('loginPage')
        else:
            messages.error(request, 'Password not the same')
            return redirect('signup')
    else:
        return render(request, 'registration.html')

