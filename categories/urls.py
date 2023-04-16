from django.urls import path
from knox import views as knox_views
from . import views


urlpatterns = [
    path('list/', views.category_list_create_view),
    path('create/', views.category_list_create_view),
    path('update/<int:pk>/', views.category_update_view),
    path('find/<int:pk>/', views.category_detail_view),
    path('delete/<int:pk>/', views.category_destory_view),

]
