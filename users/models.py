from django.db import models
from accounts.models import User


class ActivationModel(models.Model):
    user_id = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, null=True)
    token = models.CharField(max_length=1000, blank=True)


class PasswordTokenModel(models.Model):
    user_id = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, null=True)
    token = models.CharField(max_length=1000, blank=True)
