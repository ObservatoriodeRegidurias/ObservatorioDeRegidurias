from django.shortcuts import render
from apps.cabildo.models import SesionesCabildo
import locale
from django.views import View
from apps.cabildo.filters import SesionesCabildoFilter
# Create your views here.
class CabildoView(View):
    def get(self, request, *args, **kwargs):
        cabildo =  SesionesCabildo.objects.all().order_by('-created_at')
        cabildo_filter = SesionesCabildoFilter(request.GET, queryset=cabildo)
        return render(request, 'cabildo/template.html',{'filter': cabildo_filter})
