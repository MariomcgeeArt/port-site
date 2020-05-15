from django.contrib import admin
from django.urls import include, path
from . import views
import messageboard

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]