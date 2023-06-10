from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib import messages
from django.contrib.auth.models import Group

from django.views.generic.list import ListView
from django.contrib import messages
from .forms import CreateUserForm, Create_Task
from .forms import CreateGroupForm



from . models import *



def index(request):
    return render(request, 'index.html')

def sing_up(request):
    create_user_form = CreateUserForm()
    if request.method == 'POST':
        create_user_form = CreateUserForm(request.POST)
        if create_user_form.is_valid():
            user = create_user_form.save()
            username = create_user_form.cleaned_data.get('username')

            nuevo_estudiante = Group.objects.get(name='Estudiante')
            user.groups.add(nuevo_estudiante)
            Estudiante.objects.create(
                estudiante=user
            )

            messages.success(request, 'La cuenta de ' + username + ' fue creada con exito')
            return redirect('sing_in')
    
    context={'form': create_user_form}
    return render(request, 'login/sing_up.html', context)

def sing_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'Lider':
                    return redirect('account')
                if group == 'Admin':
                    return redirect('home')
                else:
                    return redirect('estudiante')

            # return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context={}
    return render(request, 'login/sing_in.html', context)

def logout_user(request):
    logout(request)
    return redirect('sing_in')


@login_required(login_url='sing_in')

def home(request): 
    tareas = Tarea.objects.all()
    grupos = Grupo.objects.all()
    lideres = Lider.objects.all()
    estudiantes = Estudiante.objects.all()

    grupos_totales = grupos.count()
    tareas_totales = tareas.count()

    context = {'tareas':tareas, 'grupos':grupos, 'lideres': lideres, 'grupos_totales':grupos_totales, 'tareas_totales': tareas_totales, 'estudiantes':estudiantes}

    return render(request, 'dashboard/dashboard.html', context)
    

class ListarUsuarios(ListView):
    model = User
    context_object_name = 'Usuarios'
    template_name = 'users/listar_usuarios.html'
    ordering = ['last_name']

login_required(login_url='sing_in')
def lider(request, id):
    lider = Lider.objects.get(lider_id=id)

    grupos = lider.grupo_set.all()
    grupos_count = grupos.count()

    context = {'lider':lider, 'grupos':grupos, 'grupos_count':grupos_count}
    return render(request, 'users/lider.html', context)


@login_required(login_url='sing_in')
def estudiante(request, id):
    estudiante = Estudiante.objects.get(estudiante_id=id)

    grupos = estudiante.grupo_set.all()
    grupos_count = grupos.count()

    context ={'estudiante':estudiante, 'grupos':grupos, 'grupos_count': grupos_count}

    return render(request, 'users/estudiante.html', context)


def accountSettings(request):
    
    return render(request, 'users/account_settings.html')


@login_required(login_url='sing_in')
def group(request):
    grupos = Grupo.objects.all()

    context = {'grupos': grupos}

    return render(request, 'groups/groups.html',context)


@login_required(login_url='sing_in')
def create_group(request):
    form = CreateGroupForm()

    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
    
    context = {'form':form}
    return render(request, 'groups/create_group.html', context)

@login_required(login_url='sing_in')
def group_detail(request, id):
    grupos = get_object_or_404(Grupo, id=id)
    tareas = Tarea.objects.filter(grupo_id = id)

    context = {'grupos': grupos, 'tareas': tareas}

    return render(request, 'groups/group_detail.html',context)


@login_required(login_url='sing_in')
def tasks(request):
    tareas = Tarea.objects.all()
    context = {'tareas' : tareas}
    return render(request, 'tasks/tasks.html', context)


@login_required(login_url='sing_in')
def create_task(request):
    grupo = Grupo.objects.all()
    form = Create_Task(initial={'grupo':grupo})

    if request.method == 'POST':
        form = Create_Task(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
        
    context = {'form':form}
    return render(request, 'tasks/create_task.html', context)

