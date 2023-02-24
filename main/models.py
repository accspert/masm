from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


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



# new model structre with foregion keys 
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    instructor_name = models.CharField(max_length=255)
    duration = models.IntegerField()

class CourseSchedule(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=30, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()                            