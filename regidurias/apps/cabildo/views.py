from django.shortcuts import render
from apps.cabildo.models import SesionesCabildo
import locale
from django.views import View

# Create your views here.
class CabildoView(View):
    def get(self, request, *args, **kwargs):
        cabildo =  SesionesCabildo.objects.all().order_by('-created_at')
        return render(request, 'cabildo/template.html', locals())
