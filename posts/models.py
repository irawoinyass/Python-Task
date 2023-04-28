from django.db import models
from django.utils import timezone
from datetime import date
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=1000, blank=False)
    body = models.TextField(blank=False)
    category_id = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, null=True)
    posted_at = models.DateField(default=date.today)
    is_public = models.BooleanField(default=False)


class Comment(models.Model):
    post_id = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey(
        "posts.Comment", related_name='comment_parent_id', on_delete=models.CASCADE, null=True, default=None)
    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, null=True)
    cat_id = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=250, blank=False)
    created_at = models.DateField(auto_now_add=True)
