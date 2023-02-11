from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import views 
from rest_framework.response import Response
from .models import BlogDataModel

# Create your views here.
def dummyData(request):
    data = {
        "name" : "max",
        "title" : "firstPost",
        "description" : "dummy data"
    }
    return JsonResponse(data)
    

class FirstAPIView(views.APIView):
    def get(self, request):
        data = {
        "name" : "max",
        "title" : "firstPost",
        "description" : "dummy data"
            }
        return Response(data)
    
    def post(self, request):
        print(request.data)
        BlogDataModel.objects.create(
            name = request.data["name"],
            title = request.data["title"],
            description = request.data["description"]

        )
        return Response(request.data)



