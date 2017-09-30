from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from core.views import home, new, edit, search, RepositorieViewSet

router = routers.DefaultRouter()
router.register(r'repositories', RepositorieViewSet)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^novo/', new, name='novo'),
    url(r'^editar/', edit, name='editar'),
    url(r'^pesquisar/', search, name='pesquisar'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
