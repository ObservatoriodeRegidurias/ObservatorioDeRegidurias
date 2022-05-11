from apps.cabildo.models import SesionesCabildo
import django_filters
 
class SesionesCabildoFilter(django_filters.FilterSet):
    class Meta:
        model = SesionesCabildo
        fields = ['entidades', 'municipio','tipo_de_sesion', ]