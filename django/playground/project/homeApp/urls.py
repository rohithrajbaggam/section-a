from django.urls import path 
from .views import helloWorld, helloName, helloHtml, helloNameHtml

urlpatterns = [
    path("home/", helloHtml, name="helloHtml"),
    path("home/<name>/", helloNameHtml, name="helloNameHtml")
    # path("home/", helloWorld, name="helloWorld"),
    # path("home/<name>/", helloName, name="helloName")

]


