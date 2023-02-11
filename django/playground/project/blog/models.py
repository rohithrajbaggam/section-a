from django.db import models

# Create your models here.
class BlogDataModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title



