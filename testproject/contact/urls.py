from django.urls import path
from .import views

urlpatterns =[
    path('register', views.registerPage, name='registerPage'),
    # path('kk', views.kk, name='kk'),
    path('home',views.home, name='home'),
    path('',views.loginPage, name= 'loginPage'),
    # path('mm',views.mm, name='mm'),
    path('login',views.login, name='login'),
    path('signup',views.signup,name='signup'),
]