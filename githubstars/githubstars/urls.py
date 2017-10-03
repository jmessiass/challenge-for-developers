from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from core.views import home, new, edit, search, create_project, update_tags, find_by_tag, RepositorieViewSet

router = routers.DefaultRouter()
router.register(r'repositories', RepositorieViewSet)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^novo/', new, name='novo'),
    url(r'^editar/', edit, name='editar'),
    url(r'^pesquisar/', search, name='pesquisar'),
    url(r'^criar-projeto/', create_project, name='criar-projeto'),
    url(r'^atualizar-tags/', update_tags, name='atualizar-tags'),
    url(r'^procurar-tags/', find_by_tag, name='procurar-tags'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
