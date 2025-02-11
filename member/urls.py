from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("info/", UserInfoView.as_view(), name="info"),
    path("state/", UserStateView.as_view()),
]
