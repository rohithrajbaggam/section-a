from django.contrib import admin
from .models import BlogDataModel, UserDetailsModel
# Register your models here.

admin.site.register(BlogDataModel)
admin.site.register(UserDetailsModel)
