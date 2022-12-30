from django.shortcuts import render, redirect
from django.http import HttpResponse
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
            messages.info(request, 'Username already taken')
            return redirect('registration')
            

        elif(User.objects.filter(email=email).exists()):
            messages.info(request, 'email already registered')
            return redirect('registration')

        else:
            if(password1 != password2):
                messages.info(request, 'password not match to confirm password')
                return redirect('registration')

            else:
                user = User.objects.create_user(
                    first_name=firstname, last_name=lastname, email=email, password=password1, username=username)
                user.save()
                auth.login(request, user)
                messages.info(request, 'registration succesful')
                return redirect('index')
    
    else:
        return render(request, 'Registration.html')
    
def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)

        user = auth.authenticate(username=username, password=password)
        user1 = User.objects.filter(username=username)

        user1.lastname = "sharma"

        print("user = ", user, "user1 = ", user1)

        if(user is not None):
            auth.login(request, user)
            messages.info(request, 'login succesful')
            return redirect('index')
            # return ("login yes")
        
        else:
            messages.info(request, 'wrong credentials')
            return redirect('login')
            # return ("no")
        
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('index')
