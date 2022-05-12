from django.shortcuts import render
from apps.cabildo.models import SesionesCabildo
import locale
from django.views import View
from apps.cabildo.filters import SesionesCabildoFilter
from django.http import HttpResponse
# Create your views here.
class CabildoView(View):
    def get(self, request, *args, **kwargs):
        cabildo =  SesionesCabildo.objects.all().order_by('-created_at')
        cabildo_filter = SesionesCabildoFilter(request.GET, queryset=cabildo)
        return render(request, 'cabildo/template.html',{'filter': cabildo_filter})

def descargar(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response=HttpResponse(fh.read(),content_type='application/actas')
            response['Content-Disposition']='inline;filename=' + os.path.basename(file_path)
            return response
        raise Http404
