from django.urls import path
from .views import *

urlpatterns = [
    path("apply/", ApplyAPIView.as_view()),
    path("edit/", ApplicationEditAPIView.as_view()),
    path("list/", ApplicationListAPIView.as_view()),
    path("submit/<int:pk>/", ApplicationSubmitAPIView.as_view()),
]