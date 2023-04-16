from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name="index"),
    path('create_user/', views.create_user, name="create_user"),
    path('create_group/', views.create_group, name="create_group"),
    path('grouplist/', views.grouplist, name="grouplist"),
]
