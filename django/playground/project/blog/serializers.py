from rest_framework import serializers
from .models import BlogDataModel, UserDetailsModel
from django.contrib.auth import get_user_model


class RegsitrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password", "confirm_password"] 
    
    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError({
                "message" : "Password does'nt match"
            })
        if len(data["password"]) < 8:
            raise serializers.ValidationError({
                "message" : "Password must be atleast 8 charaters"
            })
        return data 
        
    


class BlogDataModelSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField(read_only=True)
    category_title = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = BlogDataModel
        # fields = ["id", "name","user_name", "title", "description", "create_at", "update_at"]
        fields = "__all__"
        # exclude = ["id"]
    
    def get_user_name(self, obj):
        return obj.name.name 

    def get_category_title(self, obj):
        return obj.category.title 

class UserDetailsModelSerializer(serializers.ModelSerializer):
    blog_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = UserDetailsModel
        fields = "__all__"
    
    def get_blog_count(self, obj=UserDetailsModel):
        return obj.user_detail_model_name.all().count()


