from django.urls import path
from . import views


urlpatterns = [
    path(r'result/', views.index),
    path('hello/<str:username>', views.hello),
    path('about/', views.about),
    path('', views.input)
    
]