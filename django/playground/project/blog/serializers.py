from rest_framework import serializers
from .models import BlogDataModel

class BlogDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogDataModel
        fields = ["id", "name", "title", "description", "create_at", "update_at"]



