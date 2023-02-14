from rest_framework import serializers
from .models import BlogDataModel, UserDetailsModel

class BlogDataModelSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = BlogDataModel
        fields = ["id", "name","user_name", "title", "description", "create_at", "update_at"]
        # fields = "__all__"
        # exclude = ["id"]
    
    def get_user_name(self, obj):
        return obj.name.name 

class UserDetailsModelSerializer(serializers.ModelSerializer):
    blog_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = UserDetailsModel
        fields = "__all__"
    
    def get_blog_count(self, obj=UserDetailsModel):
        return obj.user_detail_model_name.all().count()


