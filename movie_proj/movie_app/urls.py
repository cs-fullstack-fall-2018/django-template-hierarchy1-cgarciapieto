from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blockbuster/', views.index, name='blockbuster'),
    path('index/', views.movie, name='about'),
    path('testpage/', views.index, name='test'),
]