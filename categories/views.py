from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404
from admins.permissions import IsSuperUser
from .models import Category
from .serializers import CategorySerializer


# List and Create API
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


category_list_create_view = CategoryListCreateAPIView.as_view()


# Update API

class CategoryUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


category_update_view = CategoryUpdateAPIView.as_view()


# Find API
class CategoryDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


category_detail_view = CategoryDetailAPIView.as_view()

# Delete API


class CategoryDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


category_destory_view = CategoryDestroyAPIView.as_view()
