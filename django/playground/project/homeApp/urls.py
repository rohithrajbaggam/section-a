from django.urls import path 
from .views import helloWorld, helloName, helloHtml, helloNameHtml, registerView, loginView, logout_view


urlpatterns = [
    path("home/", helloHtml, name="helloHtml"),
    path("home/<name>/",
     helloNameHtml, 
     name="helloNameHtml"),
    path("register/", registerView, name="registerView"),
    path("login/",loginView, name="loginView"),
    path("logout/", logout_view, name="logout_view")
    # path("home/", helloWorld, name="helloWorld"),
    # path("home/<name>/", helloName, name="helloName")

]


