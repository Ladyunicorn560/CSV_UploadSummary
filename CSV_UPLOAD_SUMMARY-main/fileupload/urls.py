from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('', lambda request: redirect('upload_file')), 
]

