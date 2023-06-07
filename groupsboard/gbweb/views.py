from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from django.views.generic.list import ListView
from django.contrib import messages
from .forms import CreateUserForm, Create_Task
from .forms import CreateGroupForm



from . models import Grupo, Tarea, Estudiante, User



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def sing_up(request):
    return render(request, 'sing_up.html')

def sing_in(request):
    return render(request, 'sing_in.html')

def home(request): 
    tasks = Tarea.objects.all()
    groups = Grupo.objects.all()
    students = Estudiante.objects.all()

    total_groups = groups.count()
    total_tasks = tasks.count()

    context = {'tasks':tasks, 'groups':groups, 'students': students, 'total_groups':total_groups, 'total_tasks': total_tasks}

    return render(request, 'dashboard/dashboard.html', context)
    

def create_user(request):
    context = {}
    if request.method == "POST":
        # POST
        create_user_form = CreateUserForm(request.POST)
        if create_user_form.is_valid():
            nombre = create_user_form.cleaned_data["first_name"]
            apellido = create_user_form.cleaned_data["last_name"]
            email = create_user_form.cleaned_data["email"]
            # dni = create_user_form.cleaned_data["dni"]
            username = create_user_form.cleaned_data["username"]
            password = create_user_form.cleaned_data["password"]

            usuario_nuevo = User(
                nombre = nombre,
                apellido = apellido,
                email = email,
                # dni = dni,
                username = username,
                password = password,
            )
            usuario_nuevo.save()
            
            messages.add_message(request, messages.SUCCESS, 'Usuario creado con éxito')
            return redirect("users")
    else:
        # GET
        create_user_form = CreateUserForm()
    context = {'form': create_user_form}
    return render(request, 'users/create_user.html', context)

class ListarUsuarios(ListView):
    model = User
    context_object_name = 'Usuarios'
    template_name = 'users/listar_usuarios.html'
    ordering = ['last_name']

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
    tareas = Tarea.objects.filter(group_id = id)
    return render(request, 'groups/group_detail.html',{
        'groups': groups,
        'tareas': tareas
    })

def tasks(request):
    tasks = Tarea.objects.all()
    context = {'tasks' : tasks}
    return render(request, 'tasks/tasks.html', context)

def create_task(request):
    group = Grupo.objects.all()
    form = Create_Task(initial={'group':group})

    if request.method == 'POST':
        form = Create_Task(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
        
    context = {'form':form}
    return render(request, 'tasks/create_task.html', context)


