from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from uf.models import UnidaddeFomento
from uf.api.serializers import UnidadFSerializer


class UnidadFomentoApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UnidadFSerializer
    queryset = UnidaddeFomento.objects.all()
    
