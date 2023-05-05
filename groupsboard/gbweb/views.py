from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

from .forms import CreateUserForm
from .forms import CreateGroupForm


def index(request):
    # print(reverse('index'))
    # print(request.method)

    # Esta es una lista de usuarios simulados

    user_list = [
        {'display_name': 'Carlos', 'id': '1', 'display_img': 'https://source.unsplash.com/featured/200x200', 'age': '25', 'joined': False},
        {'display_name': 'Juan', 'id': '2', 'age': '40', 'joined': True, 'groups': [1,2,3]},
        {'display_name': 'Maria', 'id': '3', 'age': '38', 'joined': True, 'groups': [1,2,3]},
        {'display_name': 'Laura', 'id': '4', 'age': '22', 'joined': True, 'groups': [1,2,3]},
        {'display_name': 'Pedro', 'id': '5', 'age': '45', 'joined': True, 'groups': [1,2,3]},
    ]

    context = {
        'simulated_users': user_list[0],
    }

    return render(request, 'gbweb/index.html', context)

def create_user(request):
    if request.method == "POST":
        # POST
        create_user_form = CreateUserForm(request.POST)
    else:
        # GET
        create_user_form = CreateUserForm()

    context = {'form': create_user_form}
    return render(request, 'gbweb/create_user.html', context)

def userprofile(request):
    # Esta es una lista de usuarios simulados

    user_list = [
        {'display_name': 'Carlos', 'id': '1', 'display_img': 'https://source.unsplash.com/featured/200x200', 'age': '25', 'joined': False},
        {'display_name': 'Juan', 'id': '2', 'display_img': 'https://source.unsplash.com/featured/200x200', 'age': '40', 'joined': True, 'groups': [1,2,3]},
        {'display_name': 'Maria', 'id': '3', 'display_img': 'https://source.unsplash.com/featured/200x200', 'age': '38', 'joined': True, 'groups': [2,8,9]},
        {'display_name': 'Laura', 'id': '4', 'display_img': 'https://source.unsplash.com/featured/200x200', 'age': '22', 'joined': True, 'groups': [1,2,3]},
        {'display_name': 'Pedro', 'id': '5', 'display_img': 'https://source.unsplash.com/featured/200x200', 'age': '45', 'joined': True, 'groups': [1,2,3]},
    ]

    context = {
        'simulated_users': user_list[2],
    }

    return render(request, 'gbweb/userprofile.html', context)

def create_group(request):
    if request.method == "POST":
        # POST
        create_group_form = CreateGroupForm(request.POST)
    else:
        # GET
        create_group_form = CreateGroupForm()

    context = {'form': create_group_form}
    return render(request, 'gbweb/create_group.html', context)

def group(request):
    return render(request, 'gbweb/group.html')

def grouplist(request):
    return render(request, 'gbweb/grouplist.html')




