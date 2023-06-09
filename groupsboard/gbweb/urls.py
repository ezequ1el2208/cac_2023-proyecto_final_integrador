from django.urls import path
from . import  views

urlpatterns = [
    path('sing_up/', views.sing_up, name='sing_up'),
    path('sing_in/', views.sing_in, name='sing_in'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    
    path('userprofile/<str:id>/', views.userprofile, name="userprofile"),
    path('create_group/', views.create_group, name="create_group"),
    path('groups/', views.group, name="groups"),
    path('group_detail/<int:id>', views.group_detail, name="group_detail"),
    path('about/', views.about, name='about'),
   
    path('create_task/', views.create_task, name='create_task'),
    path('tasks/', views.tasks, name='tasks'),
    path('users/', views.ListarUsuarios.as_view(), name="users"),
]
