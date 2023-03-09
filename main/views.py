from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .models import Student, Teacher


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "base.html")


class StudentView(TemplateView):
    def get(self, request, *args, **kwargs):
        # fetch student data
        students = Student.objects.all()
        context = {"students": students}
        return render(request, "students.html", context)


class TeacherView(TemplateView):
    def get(self, request, *args, **kwargs):
        # fetch teachers data
        teachers = Teacher.objects.all()
        context = {"teachers": teachers}
        return render(request, "teachers.html", context)


class AddRecordView(TemplateView):
    def get(self, request, record_type, *args, **kwargs):
        return render(request, "add_record.html", {'record_type': record_type})

    def post(self, request, record_type, *args, **kwargs):
        if record_type == "teachers":
            model = Teacher
        else:
            model = Student

        name = request.POST.get('name')
        surname = request.POST.get('surname')
        birthdate = request.POST.get('birthdate')
        street_nr = request.POST.get('street_nr')
        model.objects.create(name=name, surname=surname,
                             birthdate=birthdate, street_nr=street_nr)
        return redirect(f"/{record_type}")


class UpdateRecordView(TemplateView):

    def get(self, request, record_type, id, *args, **kwargs):

        if record_type == "teachers":
            record = Teacher.objects.get(id=id)
            template_name = "teachers.html"
        else:
            record = Student.objects.get(id=id)
            template_name = "students.html"

        context = {"data": record, "update": True}
        return render(request, template_name, context)

    def post(self, request, record_type, id, *args, **kwargs):

        if record_type == "teachers":
            record = Teacher.objects.get(id=id)
        else:
            record = Student.objects.get(id=id)

        # get data from template
        record.name = request.POST.get('name')
        record.surname = request.POST.get('surname')
        record.birthdate = request.POST.get('birthdate')
        record.street_nr = request.POST.get('street_nr')
        record.save()
        return redirect(f"/{record_type}")


class DeleteRecordView(TeacherView):
    def get(self, request, record_type, id, *args, **kwargs):
        if record_type == "teachers":
            Teacher.objects.get(id=id).delete()
        else:
            Student.objects.get(id=id).delete()
        return redirect(f"/{record_type}")
