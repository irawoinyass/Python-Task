from django.urls import path
from knox import views as knox_views
from . import views


urlpatterns = [
    path('login/', views.login_api),  # Login
    path('dashboard/', views.dashboard),  # Login
    path('posts/', views.fetch_posts),  # Login
    path('info/', views.get_admin_data),  # Admin Data
    path('create-adminuser/', views.create_admin_user),  # Create Adminuser
    path('update-adminuser/<int:pk>/',
         views.adminuser_update_view),  # Update Adminuser
    path('find-adminuser/<int:pk>/',
         views.adminuser_detail_view),  # Update Adminuser
    path('list-adminusers/',
         views.adminuser_list_view),  # List Adminusers
    path('delete-adminuser/<int:pk>/',
         views.adminuser_destory_view),  # Delete Adminuser
    path('logout/', knox_views.LogoutView.as_view()),  # Logout
    path('logoutall/', knox_views.LogoutAllView.as_view()),  # general Logout
]
