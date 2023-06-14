from django.urls import path
from . import  views

urlpatterns = [
    path('sing_up/', views.sing_up, name='sing_up'),
    path('sing_in/', views.sing_in, name='sing_in'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('', views.index, name="index"),
    path('home', views.home, name="home"),

    path('lider/<str:id>/', views.lider, name="lider"),
    path('estudiante/<str:id>/', views.estudiante, name="estudiante"),
    path('user_lider/', views.user_lider, name="user_lider"),
    path('user_estudiante/', views.user_estudiante, name="user_estudiante"),
    path('ver_estudiantes/<int:id>/', views.ver_estudiantes, name="ver_estudiantes"),
    path('account/', views.accountSettings, name='account'),


    path('create_group/', views.create_group, name="create_group"),
    path('groups/', views.group, name="groups"),
    path('group_detail/<int:id>/', views.group_detail, name="group_detail"),
    path('update_group/<str:pk>/', views.updateGroup, name="update_group"),
    path('delete_group/<str:pk>/', views.deleteGroup, name="delete_group"),
   
    path('create_task/', views.create_task, name='create_task'),
    path('tasks/', views.tasks, name='tasks'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),

    path('users/', views.ListarUsuarios.as_view(), name="users"),
]
