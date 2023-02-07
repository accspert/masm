from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self):
        return self.name
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthdate = models.DateField()
    street_nr = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.surname}'
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthdate = models.DateField()
    street_nr = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.surname}'
