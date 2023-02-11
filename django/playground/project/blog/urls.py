from .views import dummyData, FirstAPIView
from django.urls import path 

urlpatterns = [ 
    path("test-api/", dummyData, name="dummyData"),
    path("first-api/", FirstAPIView.as_view(), name="FirstAPIView" )
]
