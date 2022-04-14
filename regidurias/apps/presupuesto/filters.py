from apps.presupuesto.models import Presupuesto
import django_filters
 
class PresupuestoFilter(django_filters.FilterSet):
    class Meta:
        model = Presupuesto
        fields = ['entidades', 'municipio', 'presupuesto', ]