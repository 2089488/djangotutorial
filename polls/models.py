import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField('question', max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question_text = models.ForeignKey(Question)
    choice_text = models.CharField('choice', max_length=200)
    votes = models.IntegerField('number of votes:', default=0)