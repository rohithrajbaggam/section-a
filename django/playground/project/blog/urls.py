from .views import dummyContent, BlogDataModelListAPIView, BlogDataModelGetAPIView, BlogModelGenericApiView, BlogModelGenericListCreateView, BlogModelGETGenericAPIView, UserBlogModelGETGenericAPIView, UserDetailsModelGenericAPIView, BlogDataGenericListAPIView, RegsitrationGenericAPIView, BlogDataOFMeListAPIView
from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [ 
    path("blogs/me/", BlogDataOFMeListAPIView.as_view(), name="BlogDataOFMeListAPIView"),

    path("fiter-blog-list/", BlogDataGenericListAPIView.as_view(), name="BlogDataGenericListAPIView"),
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
    path("register/", RegsitrationGenericAPIView.as_view(), name="RegsitrationGenericAPIView"),
    # Jwt Authentication APIS
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
