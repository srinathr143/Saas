from django.contrib import admin
from django.urls import path
from .views import demo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', demo),
]
