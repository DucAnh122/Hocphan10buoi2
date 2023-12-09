from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('',views.store,name='store'),
    path('register/', views.register, name = 'register')
    path('login/', views.login, name = 'login')
]
