from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from ...models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefualtPagination

"""
from rest_framework.decorators import api_view,permission_classes

@api_view()
def postDetail(request,id):
    try:
        post = Post.objects.get(pk=id)
        serializer = PostSerializer(post)

        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({'detail':"post does not exist"},status=status.HTTP_404_NOT_FOUND)
------------------------------------------------------------------------------------------
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
------------------------------------------------------------------------------------------ 
@api_view(["GET","PUT","DELETE"])
def postDetail(request,id):
    post = get_object_or_404(Post,pk=id,status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"item removed successfuly"})
    

        """


'''    
class PostList(APIView):
    """
    View to list all posts.

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """
    
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer 
    def get(self,request):
        """
        Return a list of all posts.
        """
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    def post(self,request):
        """
        Create a post with provided data.
        """
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class PostDetail(APIView):
    """"""
    
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self,request,id):
        post = get_object_or_404(Post,pk=id,status=True)       
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request,id):
        post = get_object_or_404(Post,pk=id,status=True)       
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        post = get_object_or_404(Post,pk=id,status=True)       
        post.delete()
        return Response({"detail":"item removed successfuly"})'''


class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostModelViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "author", "status"]
    search_fields = [
        "=title",
    ]
    ordering_fields = ["published_date"]
    pagination_class = DefualtPagination


class CategoryModelViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
