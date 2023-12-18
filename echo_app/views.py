from django.shortcuts import render

def sign_up(request):
    return render (request,'auth-sign-up.html')

def sign_in(request):
    return render (request,'auth-sign-in.html')

def create(request):
    return render (request,'create.html')

def sign_out(request):
    return render (request, 'auth-sign-out.html')
