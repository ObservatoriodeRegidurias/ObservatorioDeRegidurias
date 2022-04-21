from apps.normatividad.models import Normatividad
import django_filters
 
class NormatividadFilter(django_filters.FilterSet):
    class Meta:
        model = Normatividad
        fields = ['entidades', 'municipio', 'tipo', ]