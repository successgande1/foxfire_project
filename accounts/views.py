from django.shortcuts import render, redirect

from django.contrib import messages, auth

from django.contrib.auth.models import User

# Create your views here.
def login(request):
    #Check if the user request came through POST method
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #This where to login the user
        user = auth.authenticate(username=username, password=password)
        #Check to see whether user inputs corresponds with the ones in Database
        if user is not None:
            #Login User
            auth.login(request, user)
            #Display success Message
            messages.success(request, 'Login Success!')
            #Redirect the User to His Dashboard
            return redirect('dashboard')
        else:
            #Notify User for Invalid Login
            messages.error(request, 'Invalid Login Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        #Create Form Variables and Assign post request 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email Already Taken')
                    return redirect('register')
                else:
                    user =  User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'Your Registration is Successful')
                    return redirect('login')

        
        else:
            messages.error(request, 'Password Did NOT Match')
            return redirect('register')
            
        
    else:

        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    #Check whether the request came through POST method
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are logged Out')
        return redirect('login')
