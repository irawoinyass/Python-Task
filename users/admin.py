from django.contrib import admin
from .models import ActivationModel, PasswordTokenModel

admin.site.register(ActivationModel)
admin.site.register(PasswordTokenModel)
