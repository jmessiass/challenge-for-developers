from django.shortcuts import render
from .models import Repositorie
from django.http import JsonResponse
from githubstars.serializers import RepositorieSerializer
from rest_framework import viewsets
import requests
import json


def home(request):
    """ initial page """
    return render(request, 'index.html')


def new(request):
    """ new repositorie page """
    if request.method == 'POST':
        url = 'https://api.github.com/users/%s/starred' % request.POST.get('uid')
        return_url = requests.get(url)

        if return_url.ok:
            repositories = json.loads(return_url.text)
            total = len(repositories)

            for repositorie in repositories:
                data = {'repositorie_id': repositorie.get('id'),
                        'name': repositorie.get('name'),
                        'url': repositorie.get('html_url'),
                        'language': repositorie.get('language')}

                serializer = RepositorieSerializer(data=data)

                if serializer.is_valid():
                    serializer.save()

            return JsonResponse(data={'total': total, 'status': 201})
        else:
            return JsonResponse(data={'status': 400})

    return render(request, 'new.html')


def remove_tag_duplicate(tags):
    """ remove tag duplicated """
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
        projects = Repositorie.objects.get(repositorie_id=id_project)
        serializer = RepositorieSerializer(projects, many=False)
        return JsonResponse(serializer.data, safe=False)

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
        'projects': Repositorie.objects.all().order_by('name'),
        'validation': validation
    }

    return render(request, 'edit.html', context)


def search(request):
    """ search repositorie page """
    return render(request, 'search.html')


class RepositorieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Repositorie.objects.all().order_by('name')
    serializer_class = RepositorieSerializer
