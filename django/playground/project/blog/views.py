from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import views, status 
from rest_framework.response import Response
from .models import BlogDataModel
from .serializers import BlogDataModelSerializer
# Create your views here.
def dummyContent(request):
    data = {
        "id" : 1,
        "name" : "max",
        "title" : "First Post",
        "description" : "Dummy Post"
    }
    return JsonResponse(data)

class BlogDataModelListAPIView(views.APIView):
    def get(self, request):
        queryset = BlogDataModel.objects.all()
        serializer = BlogDataModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        # print(request.data)
        serializer = BlogDataModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Data Inserted"}, 
                    status=status.HTTP_200_OK)
        else:
            return Response({"message" : f"Something went wrong, {serializer.errors}"},
                            status=status.HTTP_400_BAD_REQUEST)
        

class BlogDataModelGetAPIView(views.APIView):
    # def get(self, request, id):
    #     query = BlogDataModel.objects.get(pk=id)
    #     serializer = BlogDataModelSerializer(query, many=False)
    #     return Response(serializer.data)
    # def get(self, request, id):
    #     try:
    #         query = BlogDataModel.objects.get(pk=id)
    #         serializer = BlogDataModelSerializer(query, many=False)
    #         return Response(serializer.data)
    #     except Exception as e:
    #         return Response({"message" : f'Something went wrong. {e}'})

    def get(self, request, id):
        query = BlogDataModel.objects.filter(pk=id).last()
        if not query:
            return Response({"message" : "Query does not found with the ID"},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = BlogDataModelSerializer(query, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        query = BlogDataModel.objects.filter(pk=id).last()
        if not query:
            return Response({"message" : "Query does not found with the ID"},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = BlogDataModelSerializer(instance=query, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Data Updated"}, 
                        status=status.HTTP_200_OK)
            else:
                return Response({"message" : f"Something went wrong, {serializer.errors}"},
                                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        query = BlogDataModel.objects.filter(pk=id).last()
        if not query:
            return Response({"message" : "Query does not found with the ID"},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            query.delete()
            return Response({"message" : "Query was deleted"}, status=status.HTTP_200_OK)

    # def put(self, request, id):
    #     queryset = BlogDataModel.objects.get()












# def dummyData(request):
#     data = {
#         "name" : "max",
#         "title" : "firstPost",
#         "description" : "dummy data"
#     }
#     return JsonResponse(data)
    

# class FirstAPIView(views.APIView):
#     def get(self, request):
#         data = {
#         "name" : "max",
#         "title" : "firstPost",
#         "description" : "dummy data"
#             }
#         return Response(data)
    
#     def post(self, request):
#         print(request.data)
#         BlogDataModel.objects.create(
#             name = request.data["name"],
#             title = request.data["title"],
#             description = request.data["description"]

#         )
#         return Response(request.data)



