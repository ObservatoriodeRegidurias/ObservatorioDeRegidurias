from apps.regidurias.models import Regidurias
import django_filters
 
class RegiduriasFilter(django_filters.FilterSet):
    class Meta:
        model = Regidurias
        fields = ['genero', 'partido', 'comision_1', ]
