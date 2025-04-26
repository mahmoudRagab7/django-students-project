# info/models.py
from django.db import models

# Create your models here.


class Quote(models.Model):
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.text} - {self.author}"


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
