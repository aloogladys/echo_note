
from django.contrib import admin
from django.urls import path
from echo_app.views import login,create,index,register,success,test,logout,delete_note
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name= 'home'),
    path('register/', register),
    path('login/', login),
    path('create/', create, name ='create'),
    path('success/', success),
    path('test/',test),
    path('logout/',logout),
    path('delete/<id>/',delete_note)

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
