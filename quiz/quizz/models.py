from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserScore(models.Model):
    score = models.IntegerField(default=0)
    user = models.ForeignKey(User , on_delete=models.CASCADE , unique=True)
    class Meta:
        db_table = 'user_score'


class QuizQna(models.Model):
    q = models.CharField(max_length=1000)
    c1 = models.CharField(max_length=100)
    c2 = models.CharField(max_length=100)
    c3 = models.CharField(max_length=100)
    c4 = models.CharField(max_length=100)
    c = models.CharField(max_length=100)

    class Meta:
        db_table = 'quiz_qna'