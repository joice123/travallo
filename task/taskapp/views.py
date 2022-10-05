from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from taskapp.models import people, actor


def demo(request):
    obj = people.objects.all()
    res = actor.objects.all()
    return render(request, 'index.html', {'result': obj, 'value': res})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username):
                messages.info(request, 'username already')
                return redirect('register')
            elif User.objects.filter(password=password):
                messages.info(request, 'password already')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email,
                                                password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'incorect password')
            return redirect('register')
        return redirect('/')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
