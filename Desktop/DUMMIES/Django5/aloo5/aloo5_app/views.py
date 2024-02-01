from django.shortcuts import render

def home(request):
    return render(request, 'aloo5.html')

def page1(request):
    return render(request,'page1.html')
