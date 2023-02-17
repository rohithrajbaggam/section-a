from django.contrib import admin
from .models import BlogDataModel, UserDetailsModel, UserProfileModel, BlogCategoryModel, FileFieldModel
# Register your models here.
admin.site.register(FileFieldModel)
admin.site.register(BlogDataModel)
admin.site.register(BlogCategoryModel)
admin.site.register(UserProfileModel)
admin.site.register(UserDetailsModel)
