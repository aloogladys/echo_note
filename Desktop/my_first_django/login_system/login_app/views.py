from django.shortcuts import render


def fruit(request):
    try:
        print(request.POST['fruit'])
        print(request.POST['color'])
    except:
        pass
    
    return render(request,'fruits.html')

    
