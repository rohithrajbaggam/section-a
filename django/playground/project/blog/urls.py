from .views import dummyContent, BlogDataModelListAPIView, BlogDataModelGetAPIView
from django.urls import path 

urlpatterns = [ 
    path("blog-list/", BlogDataModelListAPIView.as_view(), name="BlogDataModelListAPIView"),
    path("blog-list/<id>/",BlogDataModelGetAPIView.as_view(), name="BlogDataModelGetAPIView"),
    # path("test-api/<id>", DummyContentAPIView.as_view(), name="DummyContentAPIView"),
    # path("first-api/", FirstAPIView.as_view(), name="FirstAPIView" )
]
