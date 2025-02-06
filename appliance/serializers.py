from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = Application
        fields = "__all__"
    def get_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')
    
class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'track', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'canSpendTime', 'portfolio']

class ApplicationlistSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    user_fullname = serializers.CharField(source='user.fullname', read_only=True)
    user_student_number = serializers.CharField(source='user.student_number', read_only=True)
    class Meta:
        model = Application
        fields = ['id', 'user_fullname', 'user_student_number', 'track', 'created_at']
    def get_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')
