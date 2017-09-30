from django.shortcuts import render
from .models import Repositorie
from django.http import HttpResponse
import requests
import json
import collections


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


def remove_tag_duplicate(tags):
    final_tags = ''
    tags_split = tags.split(',')
    tags = list(set(tags_split))
    for i, tag in enumerate(tags):
        if i == 0:
            final_tags += tag
        else:
            final_tags += ',%s' % tag

    return final_tags


def edit(request):
    """ edit repositorie page """
    validation = None
    if request.method == 'POST' and request.POST.get('uid'):

        id_project = request.POST.get('uid', 0)
        project = Repositorie.objects.get(id=id_project)
        tags = project.repositorie_tag

        return HttpResponse(tags)

    elif request.method == 'POST' and not request.POST.get('uid'):

        tags = request.POST.get('tags', None)
        final_tags = remove_tag_duplicate(tags)
        # update tags
        id_project = request.POST.get('project', 0)
        project = Repositorie.objects.get(id=id_project)
        project.repositorie_tag = final_tags
        project.save()
        validation = True

    context = {
        'projects': Repositorie.objects.all().order_by('repositorie_name'),
        'validation': validation
    }

    return render(request, 'edit.html', context)


def search(request):
    """ search repositorie page """
    return render(request, 'search.html')
