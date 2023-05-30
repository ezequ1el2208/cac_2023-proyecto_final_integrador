from django.shortcuts import render, redirect, get_object_or_404
from . models import Grupo, Tarea
from .forms import CreateUserForm
from .forms import CreateGroupForm


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def sing_up(request):
    return render(request, 'sing_up.html')

def sing_in(request):
    return render(request, 'sing_in.html')

def create_user(request):
    if request.method == "POST":
        # POST
        create_user_form = CreateUserForm(request.POST)
    else:
        # GET
        create_user_form = CreateUserForm()

    context = {'form': create_user_form}
    return render(request, 'users/create_user.html', context)

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
        'simulated_users': user_list[1],
    }

    return render(request, 'users/userprofile.html', context)


def group(request):
    groups = Grupo.objects.all()
    return render(request, 'groups/groups.html',{
        'groups': groups
    })

def create_group(request):
    if request.method == 'GET':
        return render(request, 'groups/create_group.html', {
            'form': CreateGroupForm()
        })
    else: 
        Grupo.objects.create(groupname=request.POST["groupname"], grouptype=request.POST["grouptype"], grouptheme=request.POST["grouptheme"], groupdescription=request.POST["groupdescription"],
        next_meeting=request.POST["next_meeting"])
        return redirect('groups')
    
def group_detail(request, id):
    groups = get_object_or_404(Grupo, id=id)
    tareas = Tarea.objects.filter(grupo_id = id)
    return render(request, 'groups/group_detail.html',{
        'groups': groups,
        'tareas': tareas
    })

def tasks(request):
    tasks = Tarea.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks' : tasks
    })

def create_task(request):
    return render(request, 'tasks/create_task.html')


