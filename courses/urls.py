from django.urls import path
from . import views

urlpatterns = [
    path('', views.Courses, name='Courses'),
    path('Business/', views.Business, name='Business'),
    path('Kids/', views.Kids, name='Kids'),
    path('Corporate/', views.Corporate, name='Corporate'),
    path('Housewives/', views.Housewives, name='Housewives'),
    path('Interview/', views.Interview, name='Interview'),
    path('StressManagement/', views.SM, name='StressManagement'),
    path('Coding/', views.Coding, name='Coding'),
] 
