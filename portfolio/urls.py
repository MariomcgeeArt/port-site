from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('portfolio/', include('portfolio.urls')),
    path('greet/<str:name>/', views.greet_by_name),  
    path('admin/', admin.site.urls),
]