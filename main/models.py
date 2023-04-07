from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.


# As proposal for a better structure:
# Comment it out& migrate it if you want to code more dry

'''class BaseModel(models.Model):
    """A base model uses abstract=True and is only a placeholder for similar models such as Student, Teacher"""
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthdate = models.DateField()
    street_nr = models.CharField(max_length=255)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return f"{self.name} {self.surname}"


class Student(BaseModel):
    pass


class Teacher(BaseModel):
    pass'''


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthdate = models.DateField(null=True, blank=True)
    street_nr = models.CharField(max_length=255)

    # New grade field
    grade = models.PositiveIntegerField(validators=[MaxValueValidator(15)], null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthdate = models.DateField(null=True, blank=True)
    street_nr = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Course(models.Model):
    DAYS_OF_WEEK = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]
    course_name = models.CharField(max_length=255)
    instructor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    duration = models.IntegerField(null=True)
    day_of_week = models.CharField(max_length=30, choices=DAYS_OF_WEEK, null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    def __str__(self):
        return f"{self.course_name}, {self.instructor}"


class Belt(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
