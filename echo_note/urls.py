
from django.contrib import admin
from django.urls import path
from echo_app.views import login,create,index,register,success,delete,test,logout
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name= 'home'),
    path('register/', register),
    path('login/', login),
    path('create/', create, name ='create'),
    path('success/', success),
    path('delete/', delete),
    path('test/',test),
    path('logout/',logout)

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
