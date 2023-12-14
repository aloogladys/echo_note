
from django.contrib import admin
from django.urls import path
from echo_app.views import sign_in,sign_up
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sign_up),
    path('login/', sign_in)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
