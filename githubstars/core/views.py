from django.shortcuts import render
from .models import Repositorie
import requests
import json


def home(request):
    """ initial page """
    return render(request, 'index.html')


def new(request):
    """ new repositorie page """
    validation = None
    msg = ''
    if request.method == 'POST':
        url = 'https://api.github.com/users/%s/starred' % request.POST.get('user')
        return_url = requests.get(url)

        if return_url.ok:
            repositories = json.loads(return_url.text)
            validation = True
            msg = len(repositories)

            for repositorie in repositories:
                obj_repositorie = Repositorie()
                obj_repositorie.repositorie_id = repositorie['id']
                obj_repositorie.repositorie_name = repositorie['name']
                obj_repositorie.repositorie_url = repositorie['html_url']
                obj_repositorie.repositorie_language = repositorie['language']
                obj_repositorie.save()

        else:
            validation = False
            msg = 'Não foi possível encontrar este usuário!'

    context = {
        'validation': validation,
        'msg': msg
    }

    return render(request, 'new.html', context)


def edit(request):
    """ edit repositorie page """
    context = {
        'projects': Repositorie.objects.all().order_by('repositorie_name')
    }
    return render(request, 'edit.html', context)


def search(request):
    """ search repositorie page """
    return render(request, 'search.html')
