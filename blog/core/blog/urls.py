from django.urls import path
from .views import IndexView,Indexview,RedirectMaktab,PostListView
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
app_name = "blog"

urlpatterns = [
    # path('fbv-index',Indexview,name= 'fbv_index'),
    
    # path('cbv-index',TemplateView.as_view(template_name='index.html',extra_context={"name":"ali",}))
    path('cbv-index/',IndexView.as_view(),name='cbv-index'),
    # path(
    # "go-to-index/",
    # RedirectView.as_view(pattern_name="blog:cbv-index"),
    # name="go-to-index",)
    path(
        'redirect-to-maktab/<int:pk>',RedirectMaktab.as_view(),name="redirectmaktab"
    ),
    path(
        'posts/',PostListView.as_view(),name="postlist"
    )
]
