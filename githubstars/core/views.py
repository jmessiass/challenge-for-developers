from django.shortcuts import render


def home(request):
    """ initial page """
    return render(request, 'index.html')
