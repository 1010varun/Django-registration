from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def index(request):
    return render(request, 'index.html')

def registration (request):
    if(request.method == 'POST'):
        firstname = request.POST['firstName']
        lastname = request.POST['lastName']
        username = request.POST['userName']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if(User.objects.filter(username=username).exists()):
            messages.info(request, 'Username Already Taken')
            return redirect('registration')
            

        elif(User.objects.filter(email=email).exists()):
            messages.info(request, 'Email Already Registered')
            return redirect('registration')

        else:
            if(password1 != password2):
                messages.info(request, 'Password not match to Confirm Password')
                return redirect('registration')

            else:
                user = User.objects.create_user(
                    first_name=firstname, last_name=lastname, email=email, password=password1, username=username)
                user.save()
                auth.login(request, user)
                messages.info(request, 'Registration Succesful')
                return redirect('index')
    
    else:
        return render(request, 'Registration.html')
    
def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username=username, password=password)

        if(user is not None):
            auth.login(request, user)
            messages.info(request, 'Login Succesful')
            return redirect('index')
        
        else:
            messages.info(request, 'Wrong Credentials')
            return redirect('login')
        
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('index')

def forgot(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        user = User.objects.filter(username=username, email=email)

        if(len(user)):
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if (password1 != password2):
                messages.info(request, 'pPassword Not Matching')
                return redirect('forgot')
            
            else:
                user = User.objects.get(username=username)
                user.set_password(password1)
                user.save()
                messages.info(request, 'Password Updated')
                return redirect('login')

        else:
            messages.info(request, 'User Not Found')
            return redirect('index')
    else:
        return render(request, 'forgot.html')
    
