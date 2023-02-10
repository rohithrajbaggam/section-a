from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloWorld(request):
    return HttpResponse("Hello World")

def helloName(request, name):
    return HttpResponse(f"Hello, {name}")


def helloHtml(request):
    return render(request, "home.html")

def helloNameHtml(request, name):
    return render(request, "hello.html", context={
        "name" : name
    })
