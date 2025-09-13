from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from .models import Post
# Create your views here.

def Indexview(request):
    '''
    a function based view to show the index page.
    '''
    return render(request,'index.html')

class IndexView(TemplateView):
    '''
    a class based view to show the index page.
    '''
    
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs) 
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context
    
class RedirectMaktab(RedirectView):
    url = 'http://maktabkhooneh.org'
    # permanent = False
    # query_string = True
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk= kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args,**kwargs)
    
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    
    # queryset = Post.objects.all()
    
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts
    
    # template_name = "blog/post_list.html"
    


 