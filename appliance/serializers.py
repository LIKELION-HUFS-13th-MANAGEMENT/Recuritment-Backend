from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    answer4 = serializers.CharField(allow_blank=True, required=False)
    portfolio = serializers.CharField(allow_blank=True, required=False) 
    class Meta:
        model = Application
        fields = "__all__"
    def get_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')
    
class ApplySerializer(serializers.ModelSerializer):
    answer4 = serializers.CharField(allow_blank=True, required=False) 
    portfolio = serializers.CharField(allow_blank=True, required=False)
    class Meta:
        model = Application
        fields = ['id', 'track', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'canSpendTime', 'portfolio']

class ApplicationlistSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    user_fullname = serializers.CharField(source='user.fullname', read_only=True)
    user_student_number = serializers.CharField(source='user.student_number', read_only=True)
    user_phone = serializers.CharField(source='user.phone', read_only=True)
    user_grade = serializers.CharField(source='user.grade', read_only=True)
    user_major_1 = serializers.CharField(source='user.major_1', read_only=True)
    user_major_2 = serializers.CharField(source='user.major_2', read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'user_fullname', 'user_student_number', 'track', 'created_at', 'user_phone', 'user_grade', 'user_major_1', 'user_major_2']
    def get_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')
    
class ApplicationDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    answer4 = serializers.CharField(required=False)
    portfolio = serializers.CharField(required=False)
    user_fullname = serializers.CharField(source='user.fullname', read_only=True)
    user_student_number = serializers.CharField(source='user.student_number', read_only=True)
    user_phone = serializers.CharField(source='user.phone', read_only=True)
    user_grade = serializers.CharField(source='user.grade', read_only=True)
    user_major_1 = serializers.CharField(source='user.major_1', read_only=True)
    user_major_2 = serializers.CharField(source='user.major_2', read_only=True)
    class Meta:
        model = Application
        fields = "__all__"
    def get_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')
