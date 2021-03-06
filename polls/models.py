from django.db import models

from django.db import models 

class Question(models.Model): 
    questionText = models.CharField(max_length=200)
    pubDate = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choiceText = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
