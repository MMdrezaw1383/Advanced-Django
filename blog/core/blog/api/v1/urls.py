from django.urls import path, include
from . import views
from rest_framework import routers

app_name = "api-v1"

router = routers.DefaultRouter()
router.register("post", views.PostModelViewset, basename="post")
router.register("category", views.CategoryModelViewset, basename="category")


urlpatterns = [
    # path(
    #     'post/',views.postList,name="post_list"
    # ),
    # path(
    #     'post/<int:id>/',views.postDetail,name="post_detail"
    # ),
    # -----
    # path(
    #     'post/',views.PostList.as_view(),name="post_list"
    # ),
    # path(
    #     'post/<int:pk>/',views.PostDetail.as_view(),name="post_detail"
    # ),
    # -----
    # path(
    #     'post/',views.PostViewset.as_view({'get':'list','post':'create'}),name="post_list"
    # ),
    # path(
    #     'post/<int:pk>/',views.PostViewset.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name="post_detail"
    # ),
]

urlpatterns += router.urls
