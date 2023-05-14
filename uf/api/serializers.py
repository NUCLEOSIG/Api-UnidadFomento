from rest_framework.serializers import ModelSerializer

from uf.models import UnidaddeFomento


class UnidadFSerializer(ModelSerializer):
    
    class Meta:
        model = UnidaddeFomento
        fields = ['fecha', 'valor']
