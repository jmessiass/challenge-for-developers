from django.shortcuts import render


def home(request):
    """ initial page """
    return render(request, 'index.html')


def new(request):
    """ initial page """
    return render(request, 'new.html')


def edit(request):
    """ initial page """
    return render(request, 'edit.html')


def search(request):
    """ initial page """
    return render(request, 'search.html')
