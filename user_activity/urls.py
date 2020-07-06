from django.urls import path

from . import views

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('getdata', views.get_data, name='get_data'),
]
