from .views import dummyContent, BlogDataModelListAPIView, BlogDataModelGetAPIView, BlogModelGenericApiView, BlogModelGenericListCreateView, BlogModelGETGenericAPIView, UserBlogModelGETGenericAPIView, UserDetailsModelGenericAPIView
from django.urls import path 

urlpatterns = [ 
    path("generic-list-create-blog/", BlogModelGenericListCreateView.as_view(), name="BlogModelGenericListCreateView"),
    path("generic-blog-list/", BlogModelGenericApiView.as_view(), name="BlogModelGenericApiView"),
    path("generic-blog-list/<id>/", BlogModelGETGenericAPIView.as_view(), name="BlogModelGETGenericAPIView"),
    path("blog-list/", BlogDataModelListAPIView.as_view(), name="BlogDataModelListAPIView"),
    path("user-blog-list/", BlogDataModelListAPIView.as_view(), name="BlogDataModelListAPIView"),
    path("user-blog-list/<user_id>/", UserBlogModelGETGenericAPIView.as_view(), name="UserBlogModelGETGenericAPIView"),
    
    path("blog-list/<id>/",BlogDataModelGetAPIView.as_view(), name="BlogDataModelGetAPIView"),
    path("user-list/", UserDetailsModelGenericAPIView.as_view(), name="UserDetailsModelGenericAPIView"),
    # path("test-api/<id>", DummyContentAPIView.as_view(), name="DummyContentAPIView"),

    # path("first-api/", FirstAPIView.as_view(), name="FirstAPIView" )
]
