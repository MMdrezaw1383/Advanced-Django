from django.urls import path
from .views import Indexview
from django.views.generic import TemplateView


urlpatterns = [
    path('',Indexview,name= 'fbv_index'),
    path('cbv-index',TemplateView.as_view(template_name='index.html',extra_context={'name':'ali',}))
]
