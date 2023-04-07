import datetime

from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import DeleteView, CreateView

from .models import Student, Teacher, Course
from .forms import StudentForm, TeacherForm, CourseForm
from django_htmx.http import HttpResponseClientRedirect, HttpResponseClientRefresh


# login_required to guarantee that the user is authenticated, before he can interacte with the database

@login_required
def create_student(request):
    form = StudentForm
    ctx = {'form': form(), 'record_type': 'student', "partial_url": 'create_student'}

    if request.htmx:
        return TemplateResponse(request, 'partials/create_record.html', ctx)

    elif request.method == 'POST':

        form = form(request.POST or None)

        if form.is_valid():
            print("VALID")
            form.save()
            return redirect('student_list')

        else:
            messages.add_message(request, messages.ERROR, f"Failure: {form.non_field_errors()}")
            return redirect('student_list')


@login_required
def update_student(request, pk):

    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    context = {
        'form': form, 'record_type': 'student',
        'record_id': student.id, "partial_url": "update_student"
    }

    if request.htmx:
        return TemplateResponse(request, "partials/update_record.html", context)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'update_record.html', context)


class DeleteStudent(DeleteView):
    # Primary used via HTMX
    model = Student

    def get_success_url(self):
        return "/students/"


from django_filters.views import FilterView
from .filters import MyFilter


@login_required
def student_list(request):
    students = Student.objects.all()

    # Bring the filter into the existing logic
    f = MyFilter(request.GET, queryset=students)
    
    context = {'records': students, 'record_type': 'Student', 'delete_url': 'delete_student',
               'create_url': 'create_student', 'update_url': 'update_student'}
    
    # Add it to the ctx
    context["filter"] = f

    return render(request, 'record_list.html', context)


@login_required
def create_teacher(request):
    form = TeacherForm(request.POST or None)
    context = {'form': form, 'record_type': 'teacher', "partial_url": "create_teacher"}

    if request.htmx:
        return TemplateResponse(request, "partials/create_record.html", context)

    if form.is_valid():
        form.save()
        return redirect('teacher_list')

    return render(request, 'create_record.html', context)


@login_required
def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    form = TeacherForm(request.POST or None, instance=teacher)
    context = {'form': form, 'record_type': 'teacher', 'partial_url': 'update_teacher',
               'record_id': teacher.id}

    if request.htmx:
        return TemplateResponse(request, "partials/update_record.html", context)

    if form.is_valid():
        form.save()
        return redirect('teacher_list')
    return render(request, 'update_record.html', context)


@login_required
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('teacher_list')


@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {'records': teachers, 'record_type': 'Teacher',
               'create_url': 'create_teacher', 'update_url': 'update_teacher', 'delete_url': 'delete_teacher'}
    return render(request, 'record_list.html', context)


@login_required
def delete_record(request, pk, model):

    if model == "teacher":
        model = Teacher

    elif model == "student":
        model = Student

    else:
        return redirect("")

    obj = get_object_or_404(model, pk=pk)

    try:
        obj.delete()

    except Exception as e:
        print(e)
        messages.add_message(request, messages.ERROR, "Deletion failed. Retry later on")
        return redirect("")

    return redirect("")


@login_required
def create_course(request):
    form = CourseForm(request.POST or None)
    context = {'form': form, 'record_type': 'course', "partial_url": "course_create"}

    if request.htmx:
        return TemplateResponse(request, "partials/create_record.html", context)

    if form.is_valid():
        form.save()
        return redirect('course_list')

    return render(request, 'create_record.html', context)


@login_required
def update_course(request, pk):
    obj = get_object_or_404(Course, pk=pk)

    form = CourseForm(request.POST or None, instance=obj)
    context = {'form': form, 'record_type': 'course', 'partial_url': 'course_update',
               'record_id': obj.id, 'delete_url': 'course_delete'}

    if request.htmx:
        return TemplateResponse(request, "partials/update_record.html", context)

    if form.is_valid():
        form.save()
        return redirect('course_list')

    return render(request, 'update_record.html', context)


class delete_course(DeleteView):
    model = Course

    def get_success_url(self):
        return "/course/"


@login_required
def list_course(request):

    qs = Course.objects.all()
    context = {'records': qs, 'record_type': 'course',
               'create_url': 'course_create', 'update_url': 'course_update', 'delete_url': 'course_delete'}
    return render(request, 'record_list.html', context)


from .calendar import *


@login_required
def calendar_view(request, year_month: str):
    """Review Courses in a calender view"""
    dt = datetime.strptime(year_month, "%Y-%m")
    next = dt + relativedelta(months=1)
    previous = dt - relativedelta(months=1)
    ctx = {"classifier": year_month, "previous": previous.strftime('%Y-%m'), "next": next.strftime('%Y-%m')}
    cal = CourseCalendar(Course.objects.all())
    split_year_month = year_month.split('-')
    year, month = split_year_month
    ctx["cal"] = cal.formatmonth(int(year), int(month))
    return render(request, "calender.html", ctx)
