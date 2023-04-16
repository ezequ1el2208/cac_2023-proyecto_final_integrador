from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

def index(request):
    print(reverse('index'))

    context = {
        'diplayname': 'John Doe',
    }

    return render(request, 'gbweb/index.html', context)

def create_user(request):
    return render(request, 'create_user.html')

def create_group(request):
    return render(request, 'create_group.html')

def grouplist(request):
    return render(request, 'grouplist.html')
