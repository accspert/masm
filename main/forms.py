from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, EmailInput,PasswordInput,BooleanField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .models import CourseSchedule
from django import forms
from django.forms import inlineformset_factory
from .models import Course, CourseSchedule

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'instructor_name', 'duration']

class CourseScheduleForm(forms.ModelForm):
    DAY_OF_WEEK_CHOICES = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    day_of_week = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=DAY_OF_WEEK_CHOICES
    )

    class Meta:
        model = CourseSchedule
        fields = ['day_of_week', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.TimeInput(format='%H:%M'),
            'end_time': forms.TimeInput(format='%H:%M'),
        }

CourseScheduleFormSet = inlineformset_factory(
    Course,
    CourseSchedule,
    form=CourseScheduleForm,
    extra=7,
    max_num=21,
    validate_max=True,
    can_delete=True
)