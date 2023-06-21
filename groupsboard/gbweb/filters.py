import django_filters
from django_filters import CharFilter
from .models import Grupo

class GrupoFiltro(django_filters.FilterSet):
    nombre = CharFilter(field_name="nombre", lookup_expr='icontains')
    tema = CharFilter(field_name='tema', lookup_expr="icontains")
    class Meta:
        model = Grupo
        fields = '__all__'
        exclude = ['lider', 'estudiante', 'proximo_encuentro']