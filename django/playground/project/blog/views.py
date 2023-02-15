from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import views, status, generics, filters, pagination
from rest_framework.response import Response
from .models import BlogDataModel, UserDetailsModel
from .serializers import BlogDataModelSerializer, UserDetailsModelSerializer
import django_filters
from django_filters import rest_framework
# Create your views here.
class BlogDataFilterSet(django_filters.FilterSet):
    class Meta:
        model = BlogDataModel
        fields = ["name", "category"]

class BlogDataGenericListAPIView(generics.ListAPIView):
    queryset = BlogDataModel.objects.all()
    serializer_class = BlogDataModelSerializer
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = BlogDataFilterSet
    search_fields = ["title", "description", "name__name"]
    pagination_class = pagination.LimitOffsetPagination
    # filterset_fields = ["name", "category"]

    # def get_queryset(self):
    #     queryset = self.queryset.all()
    #     try:
    #         # print('self.request.GET["category_title"] : ', self.request.GET["category_title"])
    #         queryset = queryset.filter(category=self.request.GET["category"])
    #     except:
    #         pass 
    #     try:
    #         # print('self.request.GET["user_name"] : ', self.request.GET["user_name"])
    #         queryset = queryset.filter(name__name=self.request.GET["user_name"])
    #     except:
    #         pass 
    #     return queryset 



class UserDetailsModelGenericAPIView(generics.GenericAPIView):
    queryset = UserDetailsModel.objects.all()
    serializer_class = UserDetailsModelSerializer

    def get(self, request):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserBlogModelGETGenericAPIView(generics.GenericAPIView):
    queryset = BlogDataModel.objects.all()
    serializer_class = BlogDataModelSerializer

    def get(self, request, user_id):
        query = self.queryset.filter(name__pk=user_id)
        
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogModelGenericApiView(generics.GenericAPIView):
    queryset = BlogDataModel.objects.all()
    serializer_class = BlogDataModelSerializer

    def get(self, request):
        querset = self.queryset.all()
        serializer = self.serializer_class(querset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Data is inserted"}, status=status.HTTP_200_OK)
        else:
            return Response({"message" : f"Something went wrong, {serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
    

class BlogModelGenericListCreateView(generics.ListCreateAPIView):
    queryset = BlogDataModel.objects.all()
    serializer_class = BlogDataModelSerializer

class BlogModelGETGenericAPIView(generics.GenericAPIView):
    queryset = BlogDataModel.objects.all()
    serializer_class = BlogDataModelSerializer

    def get(self, request, id):
        query = self.queryset.filter(pk=id).last()
        if not query:
            return Response({"message" : "Id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(query, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        query = self.queryset.filter(pk=id).last()
        if not query:
            return Response({"message" : "Id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(instance=query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Data is update"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        query = self.queryset.filter(pk=id).last()
        if not query:
            return Response({"message" : "Id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        query.delete()
        return Response({"message" : "query was deleted"}, status=status.HTTP_200_OK)





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



