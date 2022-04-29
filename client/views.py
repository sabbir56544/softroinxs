from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout

# Create your views here.

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('client_signup')
 
        myuser = User.objects.create_user(username=email, password=password)
        myuser.save()     
		
	   
        messages.add_message(request, messages.SUCCESS, 'We sent you an email to verify your account')


        return redirect('client_login')
        
        
    return render(request, "client/signup.html")


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['password']
        
        user = authenticate(username=email, password=pass1)
        
        if user is not None:
            django_login(request, user)
            # messages.success(request, "Logged In Sucessfully!!")
            return redirect('client_home')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('client_home')
    
    return render(request, "client/login.html")



def client_home(request):
	return render(request, 'client/home.html')


def log_out_view(request):
    logout(request)
    return redirect('client_login')