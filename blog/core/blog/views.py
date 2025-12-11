from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PostForm
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# Create your views here.


def Indexview(request):
    """
    a function based view to show the index page.
    """
    return render(request, "index.html")


class IndexView(TemplateView):
    """
    a class based view to show the index page.
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context


class RedirectGithub(RedirectView):
    url = "https://github.com/MMdrezaw1383"

    # permanent = False
    # query_string = True
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "blog.view_post"
    model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = "-id"
    # queryset = Post.objects.all()

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts

    # template_name = "blog/post_list.html"


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    # template_name = "post_form.html"
    form_class = PostForm
    # fields = ['title', 'content','status','category','published_date']
    success_url = "/blog/posts/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    # template_name = "post_form.html"
    # fields = ['title', 'content','status','category','published_date']
    form_class = PostForm
    success_url = "/blog/posts/"


class PostDeleteView(DeleteView):
    model = Post
    # template_name = "post_confirm_delete.html"
    success_url = "/blog/posts/"
