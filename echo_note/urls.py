
from django.contrib import admin
from django.urls import path
from echo_app.views import logout,login,create,index,register
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('register/', register),
    path('login/', login),
    path('create/', create)

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
