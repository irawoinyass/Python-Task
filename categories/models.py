from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=120, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
