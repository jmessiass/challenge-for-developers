from django.conf.urls import url
from django.contrib import admin
from core.views import home, new, edit, search

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^novo/', new, name='novo'),
    url(r'^editar/', edit, name='editar'),
    url(r'^pesquisar/', search, name='pesquisar'),
    url(r'^admin/', admin.site.urls),
]
