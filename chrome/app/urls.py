from django.urls import path
from . import views
urlpatterns=[
    path('',views.chrome_login),
    path('home',views.home),
    path('chrome_logout',views.chrome_logout),
    path('add_prod',views.add_prod),
    path('edit/<pid>',views.edit),
    path('delete/<pid>',views.delete),



    path('register',views.register),
    path('user_home',views.user_home),
]