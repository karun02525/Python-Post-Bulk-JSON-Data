from django.db import models

# Create your models here.

class ExamCenter(models.Model):
    cname = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    
class Student(ExamCenter):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()    


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=20)
    