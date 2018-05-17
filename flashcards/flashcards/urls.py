
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from apis import views

router = routers.DefaultRouter()
router.register(r'ListaSlow', views.SlowaViewSet)
router.register(r'ListaDefinicji', views.DefinicjeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth', include('rest_framework.urls', namespace = 'rest_framework')),
    url(r'^admin/', admin.site.urls),
]
