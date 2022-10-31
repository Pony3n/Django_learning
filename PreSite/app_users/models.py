from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, blank=True)      #blank=True - поле может быть пустым
    date_of_birth = models.DateField(null=True, blank=True)
    nickname = models.CharField(max_length=30)