from django.urls import path, include
from .views import *
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
    # name="go-to-index",),
    # path(
    #     'redirect-to-github/<int:pk>/',RedirectGithub.as_view(),name="redirectmaktab"
    # ),
    path(
        'posts/',PostListView.as_view(),name="postlist"
    ),
    path(
        'post/<int:pk>/',PostDetailView.as_view(),name="postdetail"
    ),
    # path(
    #     'post/create/',PostCreateView.as_view(),name="createpost"
    #     ),
    # path(
    #     'post/<int:pk>/edit/',PostUpdateView.as_view(),name="editpost"
    # ),
    # path(
    #     'post/<int:pk>/delete/',PostDeleteView.as_view(),name="deletepost"
    # ),
    path("api/v1/", include("blog.api.v1.urls"))
]
