from django.urls import path

from . import views

urlpatterns = [
    path('', views.myView, name='myView'),
]