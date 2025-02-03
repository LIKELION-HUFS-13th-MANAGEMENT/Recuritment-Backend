from django.urls import path
from .views import *

urlpatterns = [
    path("apply/", ApplyAPIView.as_view()),
    path("edit/<int:pk>/", ApplicationEditAPIView.as_view()),
    path("list/", ApplicationListAPIView.as_view()),
]