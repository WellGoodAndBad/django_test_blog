from django.urls import path
from .views import LogInView, LogOutView, SignUpView


app_name = "users_auth"

urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
]