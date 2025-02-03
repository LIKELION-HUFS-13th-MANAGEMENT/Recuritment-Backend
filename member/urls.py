from django.urls import path
from .views import SignUpView, LoginView, LogoutView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
