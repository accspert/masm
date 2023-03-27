from django import forms
from .models import Teacher, Student, Course


class TeacherForm(forms.ModelForm):
    birthdate = forms.DateField(input_formats=[
        '%Y-%m-%d',
        '%m/%d/%Y',
        '%m/%d/%y'
    ], required=False)

    class Meta:
        model = Teacher
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class StudentForm(forms.ModelForm):
    birthdate = forms.DateField(input_formats=[
        '%Y-%m-%d',
        '%m/%d/%Y',
        '%m/%d/%y'
    ], required=False)

    class Meta:
        model = Student
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
