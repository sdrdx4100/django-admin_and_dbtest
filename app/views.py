from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_success')
        else:
            return HttpResponse('Invalid login credentials')
    return render(request, 'login.html')

def login_success(request):
    return HttpResponse('login success')
