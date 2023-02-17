from django.db import models
from django.core.validators import FileExtensionValidator
from .filevalidations import validate_file_size 
from django.contrib.auth import get_user_model

# Create your models here.

class FileFieldModel(models.Model):
    file_field = models.FileField(upload_to="media/files/", 
                                  validators=[FileExtensionValidator(
                allowed_extensions=["pdf", "jpg", "jpeg", "png", "mp4"]), 
                validate_file_size])



class UserDetailsModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    

class UserProfileModel(models.Model):
    user = models.OneToOneField(UserDetailsModel, on_delete=models.CASCADE, related_name="user_profile_model_user")
    profile_image = models.ImageField(upload_to="media/profiles/")
    bio = models.TextField()
    date_of_birth = models.DateField()

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    

class BlogCategoryModel(models.Model):
    title = models.CharField(max_length=200)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title


class BlogDataModel(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="blog_author", null=True)
    name = models.ForeignKey(UserDetailsModel, on_delete=models.CASCADE, related_name="user_detail_model_name", null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(BlogCategoryModel, on_delete=models.CASCADE, related_name="blog_category", null=True, blank=True)
    likes = models.ManyToManyField(UserDetailsModel, related_name="blog_data_model_likes",  blank=True)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"



