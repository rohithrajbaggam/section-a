from django.db import models

# Create your models here.

class UserDetailsModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.name 


class BlogDataModel(models.Model):
    name = models.ForeignKey(UserDetailsModel, on_delete=models.CASCADE, related_name="user_detail_model_name")
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title



