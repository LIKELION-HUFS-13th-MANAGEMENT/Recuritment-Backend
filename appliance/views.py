from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .permissions import IsOwnerOrReadOnly, IsSuperUserOnly
# from django.utils.timezone import make_aware
from django.utils import timezone
from datetime import datetime

try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo  

# Create your views here.
DEADLINE = timezone.make_aware(datetime(2025, 2, 23, 23, 59, 59), timezone=ZoneInfo('Asia/Seoul'))

class ApplyAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        current_time = timezone.now().astimezone(ZoneInfo("Asia/Seoul"))
        if current_time > DEADLINE:
            return Response({"error": "제출 기한이 지났습니다."}, status=status.HTTP_403_FORBIDDEN)
        if Application.objects.filter(user=request.user).exists():
            return Response({"error": "이미 신청서를 작성했습니다."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ApplySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ApplicationEditAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    def get_object(self):
        user = self.request.user
        application = get_object_or_404(Application, user=user)
        self.check_object_permissions(self.request, application)
        return application

    def get(self, request):
        application = self.get_object()
        serializer = ApplicationSerializer(application)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        current_time = timezone.now().astimezone(ZoneInfo("Asia/Seoul"))
        if current_time > DEADLINE:
            return Response({"error": "제출 기한이 지났습니다."}, status=status.HTTP_403_FORBIDDEN)
        application = self.get_object()
        serializer = ApplicationSerializer(application, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ApplicationSubmitAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        application = get_object_or_404(Application, pk=pk)
        self.check_object_permissions(self.request, application)
        return application

    def get(self, request, pk):
        application = self.get_object(pk)
        serializer = ApplicationSerializer(application)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ApplicationListAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOnly]
    def get(self, request):
        try:
            applications = Application.objects.all()
            serializer = ApplicationlistSerializer(applications, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
