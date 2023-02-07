from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from django.contrib.auth.decorators import user_passes_test,login_required
from .models import Student as StudentData , Teacher as TeacherData , Course as CourseData
# from .forms import SignupForm

# login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse('<script>alert("Password or user name is incorrect")</script>')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})
@login_required(login_url='login')
def index(request):
    return render(request, 'main/index.html',{'user': request.user} )
@login_required(login_url='login')
def Courses(request):
    data = CourseData.objects.all()
    return render(request, 'main/course.html',{'user': request.user, 'data':data} )


@login_required(login_url='login')
def create_Course(request):
    data = CourseData.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        instructor = request.POST.get('instructor')
        duration = request.POST.get('duration')
       

        Course = CourseData(name=name, instructor=instructor, duration=duration)
        Course.save()
        return redirect('Courses')

    return render(request, 'main/course.html',{'user': request.user, 'Create':True, 'data':data})


@login_required(login_url='login')
def update_Course(request, Course_id):
    data = CourseData.objects.all()
    student = CourseData.objects.get(id=Course_id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.instructor = request.POST.get('instructor')
        student.duration = request.POST.get('duration')
        student.save()

        return redirect('Courses')

    context = {'student': student , 'user': request.user, 'data':data, 'Update':True }
    return render(request, 'main/course.html', context)




@login_required(login_url='login')
def delete_Courses(request, Course_id):
    course = get_object_or_404(CourseData, pk=Course_id)
    course.delete()
    return redirect('Courses')



@login_required(login_url='login')
def Teacher(request):
    data = TeacherData.objects.all()
    return render(request, 'main/Teacher.html',{'user': request.user, 'data':data} )
@login_required(login_url='login')
def create_Teacher(request):
    data = TeacherData.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        birthdate = request.POST.get('birthdate')
        street_nr = request.POST.get('street_nr')

        student = TeacherData(name=name, surname=surname, birthdate=birthdate, street_nr=street_nr)
        student.save()
        return redirect('Teacher')

    return render(request, 'main/Teacher.html',{'user': request.user, 'Create':True, 'data':data})



@login_required(login_url='login')
def update_Teacher(request, Teacher_id):
    data = TeacherData.objects.all()
    student = TeacherData.objects.get(id=Teacher_id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.surname = request.POST.get('surname')
        student.birthdate = request.POST.get('birthdate')
        student.street_nr = request.POST.get('street_nr')
        student.save()

        return redirect('Teacher')

    context = {'student': student , 'user': request.user, 'data':data, 'Update':True }
    return render(request, 'main/Teacher.html', context)


@login_required(login_url='login')
def delete_Teacher(request, Teacher_id):
    student = get_object_or_404(TeacherData, pk=Teacher_id)
    student.delete()
    return redirect('Teacher')





@login_required(login_url='login')
def Student(request):
    data = StudentData.objects.all()
    return render(request, 'main/student.html',{'user': request.user, 'data':data} )
@login_required(login_url='login')
def create_student(request):
    data = StudentData.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        birthdate = request.POST.get('birthdate')
        street_nr = request.POST.get('street_nr')

        student = StudentData(name=name, surname=surname, birthdate=birthdate, street_nr=street_nr)
        student.save()
        return redirect('Student')

    return render(request, 'main/student.html',{'user': request.user, 'Create':True, 'data':data})



@login_required(login_url='login')
def update_student(request, student_id):
    data = StudentData.objects.all()
    student = StudentData.objects.get(id=student_id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.surname = request.POST.get('surname')
        student.birthdate = request.POST.get('birthdate')
        student.street_nr = request.POST.get('street_nr')
        student.save()

        return redirect('Student')

    context = {'student': student , 'user': request.user, 'Page':'List','data':data, 'Update':True }
    return render(request, 'main/student.html', context)


@login_required(login_url='login')
def delete_student(request, student_id):
    student = get_object_or_404(StudentData, pk=student_id)
    student.delete()
    return redirect('Student')






@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def admin_view(request):
    return render(request, 'main/admin.html',{'user': request.user} )

def logout_view(request):
    logout(request)
    return redirect('login')
def custom_404(request):
    return HttpResponse('<script>alert("Page not found") </script> ')

def custom_403(request):
    return HttpResponse('<script>alert("Access forbidden") </script>')