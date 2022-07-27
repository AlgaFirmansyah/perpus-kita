from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == 'POST':
        userna = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=userna, password=password)
        if user is not None:
            login(request, user)
            return redirect('/perpuskita')

        else : 
            messages.error(request, 'You do not have permission to access this  website.')          
            return redirect('/')

    return render(request, 'perpustakaan/login.html')