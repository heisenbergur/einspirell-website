from django.urls import path
from . import views

urlpatterns = [
    path('', views.Courses, name='Courses'),
    path('Business/', views.Business, name='Business'),
    path('Kids/', views.Kids, name='Kids'),
    path('Corporate/', views.Corporate, name='Corporate'),
] 
