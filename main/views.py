from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Teacher
from .forms import StudentForm, TeacherForm


def create_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    context = {'form': form, 'record_type': 'student'}
    return render(request, 'create_record.html', context)


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    context = {'form': form, 'record_type': 'student',
               'record_id': student.id, 'delete_url': 'delete_student'}
    return render(request, 'update_record.html', context)


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    context = {'record': student, 'record_type': 'student',
               'redirect_url': 'student_list'}
    return render(request, 'delete_record.html', context)


def student_list(request):
    students = Student.objects.all()
    context = {'records': students, 'record_type': 'Student',
               'create_url': 'create_student', 'update_url': 'update_student'}
    return render(request, 'record_list.html', context)


def create_teacher(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('teacher_list')
    context = {'form': form, 'record_type': 'teacher'}
    return render(request, 'create_record.html', context)


def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    form = TeacherForm(request.POST or None, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect('teacher_list')
    context = {'form': form, 'record_type': 'teacher',
               'record_id': teacher.id, 'delete_url': 'delete_teacher'}
    return render(request, 'update_record.html', context)


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    context = {'record': teacher, 'record_type': 'teacher',
               'redirect_url': 'teacher_list'}
    return render(request, 'delete_record.html', context)


def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {'records': teachers, 'record_type': 'Teacher',
               'create_url': 'create_teacher', 'update_url': 'update_teacher'}
    return render(request, 'record_list.html', context)
