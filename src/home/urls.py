from django.contrib import admin
from django.urls import path
from .views import demo, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', demo),
    path('about/',about),
]
