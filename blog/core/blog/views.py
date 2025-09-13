from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def Indexview(request):
    
    return render(request,'templates/index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)