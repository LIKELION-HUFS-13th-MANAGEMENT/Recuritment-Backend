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
    class Meta:
        model = Application
        fields = ['id', 'user', 'track', 'created_at']
    def get_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')
