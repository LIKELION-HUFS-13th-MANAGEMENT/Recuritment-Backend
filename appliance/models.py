from django.db import models
from member.models import *

# Create your models here.
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.IntegerField()
    answer1 = models.CharField(max_length=500)
    answer2 = models.CharField(max_length=500)
    answer3 = models.CharField(max_length=500)
    answer4 = models.CharField(max_length=300, null=True)
    answer5 = models.CharField(max_length=500)
    canSpendTime = models.BooleanField(default=True)
    portfolio = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)