from django.urls import path
from . import views 

urlpatterns =[
    path ('', views.getallData),
    path ('single/<id>', views.getoneData),
    path ('add/', views.addData),
    path ('update/<id>', views.updateData),
    path ('delete/<id>', views.deleteData),


]