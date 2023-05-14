from rest_framework.routers import DefaultRouter

from uf.api.views import UnidadFomentoApiViewSet

router_uf = DefaultRouter()

router_uf.register(
    prefix='UnidadFomento', basename='UnidadFomento', viewset=UnidadFomentoApiViewSet
)
