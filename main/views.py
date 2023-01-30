from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import user_passes_test,login_required
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
    return render(request, 'main/index.html' )
@login_required(login_url='login')
def Courses(request):
    return render(request, 'main/course.html' )
@login_required(login_url='login')
def Student(request):
    return render(request, 'main/student.html' )
@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def admin_view(request):
    return render(request, 'main/admin.html' )

def logout_view(request):
    logout(request)
    return redirect('login')
def custom_404(request):
    return HttpResponse('<script>alert("Page not found") </script> ')

def custom_403(request):
    return HttpResponse('<script>alert("Access forbidden") </script>')