from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User 
from .models import Todo


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.create(username )
        user.set_password(request.POST['password']) 
        user.save()
        
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')


def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Todo.objects.create(name = name, description=description)
    

    
    return render(request,'create.html')

def todo_list(request):
    query_set= Todo.objects.all()
    context = {'query_set':query_set}
    print(context)
    return render(request,'list.html', context)
    

def update(request,id):
    Todo.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST ['name']
        description = request.POST['description']
        todo = Todo.objects.get(id)

        todo.name(request.POST[name])
        todo.description(request.POST[description])
        todo.save()
        return render (request,'list.html')


    return render(request,'list.html')

def delete(request):
    return render(request,'delete.html')



