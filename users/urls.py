from django.urls import path
from knox import views as knox_views
from . import views


urlpatterns = [
    path('sign-up/', views.register_api),  # Registration
    path('activation/<int:user_id>/<str:confirmation_token>/',
         views.activation),  # Verification
    path('sign-in/', views.login_api),  # Login
    path('info/', views.get_user_data),  # Authenticated user data
    path('change-password/<int:pk>/', views.change_passsword),  # Change Password
    # Forget passwprd request
    path('forget-password-request/', views.forgetpassword_request),
    path('password/reset/<int:user_id>/<str:confirmation_token>/',
         views.password_rest),  # Password Reset
    path('logout/', knox_views.LogoutView.as_view()),  # Logout
    path('logoutall/', knox_views.LogoutAllView.as_view()),  # general Logout

]
