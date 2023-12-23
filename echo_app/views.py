from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.models import User
from .models import Note


def register(request):

    if request.method == 'POST':
        user = User.objects.create(username=request.POST['username'])
        user.set_password(request.POST['password'])
        user.save()
        return render(request,'success.html')

    return render(request,'auth-sign-up.html')

    
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
            
    
        if user is not None:
            login_user(request, user)
            return redirect('create')
        
        else:
            return redirect('/login')
            
        
    else:
        return render(request, 'auth-sign-in.html') 
    
    
def logout(request):
    logout_user(request)
    return redirect('login_page')   

def create(request):
    if request.user.is_authenticated == False:
        return redirect('/login')

    
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        print(title, description)
        Note.objects.create(title=title, description = description ,user = request.user)
    
    notes = Note.objects.filter(user = request.user )
    # user = request.user
    print(notes)
    context = {
        'note_queryset':notes,
        'user':request.user,
        'welcome_message':'hello world'
    }

    return render(request, 'create.html', context)



def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request,'success.html')

def delete_note(request,id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('create')

def logout(request):
    logout_user(request)
    return redirect('home')

def test(request):
    return render(request, 'test.html')

