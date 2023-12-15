from django.db import models

# Create your models here.

class Student(models.Model):
    idx = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20, null=False)
    user_id = models.CharField(max_length=40, null=False, unique=True)
    user_password = models.CharField(max_length=100, null=False)
    user_hp = models.CharField(max_length=11)
    sign_up = models.DateTimeField(auto_created=True)