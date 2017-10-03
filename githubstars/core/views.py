from django.shortcuts import render
from .models import Repository
from django.http import JsonResponse
from .serializers import RepositorySerializer
from .utils import remove_tag_duplicate
from rest_framework import viewsets
import requests
import json


def home(request):
    """ initial page """
    return render(request, 'index.html')


def new(request):
    """ new repositorie page """
    return render(request, 'new.html')


def edit(request, project_id=None):
    """ edit repositorie page """
    context = {
        'projects': Repository.objects.all().order_by('name'),
    }
    return render(request, 'edit.html', context)


def search(request):
    """ search repositorie page """
    return render(request, 'search.html')


def find_by_tag(request):
    if request.method == 'GET' and request.GET.get('uid'):
        projects = Repository.objects.filter(tag__contains=request.GET.get('uid'))
        serializer = RepositorySerializer(projects, many=True)
        return JsonResponse(serializer.data, safe=False)


def create_project(request):
    """ get repositorie from github and create in database """
    if request.method == 'POST':
        url = 'https://api.github.com/users/%s/starred' % request.POST.get('uid')
        return_url = requests.get(url)

        if return_url.ok:
            repositories = json.loads(return_url.text)
            total = len(repositories)

            for repositorie in repositories:
                data = {'repository_id': repositorie.get('id'),
                        'name': repositorie.get('name'),
                        'url': repositorie.get('html_url'),
                        'language': repositorie.get('language')}

                serializer = RepositorySerializer(data=data)

                if serializer.is_valid():
                    serializer.save()

            return JsonResponse(data={'total': total, 'status': 201})
        else:
            return JsonResponse(data={'status': 400})


def update_tags(request):
    """ create tags to the projects """
    if request.method == 'POST':
        if request.POST.get('uid'):
            id_project = request.POST.get('uid', 0)
            projects = Repository.objects.get(repository_id=id_project)
            serializer = RepositorySerializer(projects, many=False)
            return JsonResponse(serializer.data, safe=False)

        elif request.POST.get('id'):
            # update tags
            tags = request.POST.get('tags', None)
            final_tags = remove_tag_duplicate(tags)
            id_project = request.POST.get('id', 0)
            project = Repository.objects.get(repository_id=id_project)

            data = {'tag': final_tags}

            serializer = RepositorySerializer.update(request, project, data)
            serializer.save()
            return JsonResponse(data={'status': 200})


class RepositorieViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows users to be viewed or edited """
    queryset = Repository.objects.all().order_by('name')
    serializer_class = RepositorySerializer
