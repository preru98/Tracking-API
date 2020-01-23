from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    enrollmentNumber=models.CharField(primary_key=True,max_length=20)
    name=models.CharField(max_length=2000)
    course=models.CharField(max_length=2000)
    year=models.CharField(max_length=2000)
    password=models.CharField(max_length=2000)
    


class Admin(models.Model):
    adminID=models.CharField(max_length=2000)
    password=models.CharField(max_length=2000)


class Tag(models.Model):
    tagUID=models.CharField(max_length=200,primary_key=True)
    student=models.OneToOneField(Student,on_delete=models.CASCADE)


class TapTiming(models.Model):
    tapAt=models.DateTimeField(default=timezone.now)
    tag=models.ForeignKey(Tag, to_field='tagUID',on_delete=models.CASCADE)
