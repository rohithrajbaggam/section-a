from django.db import models

# Create your models here.

class UserDetailsModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.name 

class UserProfileModel(models.Model):
    user = models.OneToOneField(UserDetailsModel, on_delete=models.CASCADE, related_name="user_profile_model_user")
    profile_image = models.ImageField(upload_to="media/profiles/")
    bio = models.TextField()
    date_of_birth = models.DateField()

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.user.name

class BlogCategoryModel(models.Model):
    title = models.CharField(max_length=200)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title


class BlogDataModel(models.Model):
    name = models.ForeignKey(UserDetailsModel, on_delete=models.CASCADE, related_name="user_detail_model_name")
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(BlogCategoryModel, on_delete=models.CASCADE, related_name="blog_category", null=True, blank=True)
    likes = models.ManyToManyField(UserDetailsModel, related_name="blog_data_model_likes",  blank=True)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title



