from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import *
import datetime
# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=username, password = password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'homepage.html')
            # return redirect('homepage')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('/')
    return render(request, 'index.html')


def register(request):
    now = datetime.datetime.now()
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        btown = request.POST['btown']
        bday = request.POST['bday']
        htown = request.POST['htown']
        street = request.POST['street']
        skill = request.POST['class']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        gender = request.POST['gender']
        username = lastname +' ' +firstname

        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username Taken")
                return redirect('/register/student')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password)
                user.save()
                profile = UsersDetail.objects.create(Name=username, Gender=gender, Birthtown= btown, birth_date= bday, Street= street, Hometown=htown, Class= skill, position = "student", start_date=now.strftime("%Y-%m-%d"))
                profile.save()
                return redirect('/')
            messages.info(request, "Password mismatch")
            return redirect('/register/student')

    return render(request, 'register.html')

@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return redirect('/')

def control(request):
    user = User.objects.get(username=request.user.username)
    return render(request, 'control.html', {'user':user})

def homepage(request):
    # user = User.objects.get(username=request.user.username)
    return render(request, 'homepage.html')

def login(request):
    # user = User.objects.get(username=request.user.username)
    return render(request, 'log_in.html')