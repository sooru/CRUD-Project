from django.db import models
from django import forms
class User(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=25)
    password=models.CharField(max_length=25)
