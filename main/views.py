from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from django.contrib.auth.decorators import user_passes_test,login_required
from .models import Student as StudentData , Teacher as TeacherData , Course as CourseData  ,CourseSchedule
# from .forms import SignupForm
from .forms import CourseForm, CourseScheduleFormSet
from django.http import HttpResponseRedirect 
from django.urls import reverse
from datetime import datetime, time, timedelta


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
    classes=CourseSchedule.objects.all()
    events = []
    Days={'Sunday':0,"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}
    for class_ in classes:
        day_index = Days[class_.day_of_week]
        # Calculate the start and end times based on the current date and time
        now = datetime.now()
        start_datetime = now.replace(hour=class_.start_time.hour, minute=class_.start_time.minute, second=0, microsecond=0)
        start_datetime += timedelta(days=(day_index - now.weekday()) % 7)
        end_datetime = now.replace(hour=class_.end_time.hour, minute=class_.end_time.minute, second=0, microsecond=0)
        end_datetime += timedelta(days=(day_index - now.weekday()) % 7)
        events.append({
            'title': class_.course.course_name,
            'start': start_datetime.isoformat(),
            'end': end_datetime.isoformat()
        })
    print(events)
    return render(request, 'main/index.html',{'user': request.user,"events":events} )
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
       

        Course = CourseData(course_name=name, instructor_name=instructor, duration=duration)
        Course.save()
        return redirect('Courses')

    return render(request, 'main/course.html',{'user': request.user, 'Create':True, 'data':data})


@login_required(login_url='login')
def update_Course(request, Course_id):
    data = CourseData.objects.all()
    student = CourseData.objects.get(id=Course_id)
    Days=['Sunday',"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    newDys=[]
    for day in Days:
        newday={}
        newday['Day']=day
        
        index=1
        mysavedata=CourseSchedule.objects.filter(course=student,day_of_week=day)
        if mysavedata.__len__()>=1:
            newday['checked']=True
        else:
            newday['checked']=False
        for d in mysavedata:
            newday[f'slot_{index}_start']=d.start_time
            newday[f'slot_{index}_end']=d.end_time
            newday[f'slot_{index}_id']=d.pk
            index++1
        for i in range(index+1,4):
            newday[f'slot_{i}_start']=''
            newday[f'slot_{i}_end']=''
            newday[f'slot_{i}_id']=''
            
        newDys.append(newday)
    print(newDys)


    
    # myschedule=CourseSchedule.objects.filter(course=student)
    
    context = {'student': student , 'user': request.user, 'data':data, 'Update':True,'Days':newDys }
    if request.method == 'POST':
        student.course_name = request.POST.get('name')
        student.instructor_name = request.POST.get('instructor')
        student.duration = request.POST.get('duration')
        student.save()
        for d in Days:
            if request.POST.get(f'{d}'):
                print(d)
                myindexes=1
                for i in range(myindexes,4):
                    if request.POST.get(f'{d}-input-{i}-start')!= None:
                        try:
                            id=request.POST.get(f'{d}-input-{index}-id')
                            schedulevalue=CourseSchedule.objects.get(pk=id)
                            schedulevalue.start_time=request.POST.get(f'{d}-input-{i}-start')
                            schedulevalue.end_time=request.POST.get(f'{d}-input-{i}-end')
                            print(start_time,end_time)
                            schedulevalue.save()
                        except:
                            start_time=request.POST.get(f'{d}-input-{i}-start')
                            
                            end_time=request.POST.get(f'{d}-input-{i}-end')
                            print(start_time,end_time)
                            sc=CourseSchedule(start_time=start_time,end_time=end_time,day_of_week=d,course=student)
                            sc.save()
                        
                    
                
                

        return redirect('Courses')

    print(context)
    return render(request, 'main/course.html',context)




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




def course_update(request, course_id):
    course = get_object_or_404(CourseData, pk=course_id)
    schedules = CourseSchedule.objects.filter(course=course)
    if request.method == 'POST':
        course_form = CourseForm(request.POST, instance=course)
        schedule_formset = CourseScheduleFormSet(request.POST)
        if course_form.is_valid() and schedule_formset.is_valid():
            course_form.save()
            for form in schedule_formset:
                if form.cleaned_data:
                    schedule = form.save(commit=False)
                    schedule.course = course
                    schedule.save()
            return HttpResponseRedirect(reverse('course_detail', args=(course.id,)))
    else:
        course_form = CourseForm(instance=course)
        schedule_formset = CourseScheduleFormSet(queryset=schedules)
    return render(request, 'main/testUpdatecourse.html', {'course_form': course_form, 'schedule_formset': schedule_formset})