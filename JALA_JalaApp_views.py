from django.shortcuts import render, redirect
from JalaApp import forms
from .forms import JalaForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def Welcome_page(request):
    return render(request, 'myapp/front.html')


def Hame_Page(request):
    return render(request, 'myapp/home.html')


@login_required
def login_page(request):
    return render(request, 'registration/login.html')


def Logout_page(request):
    return render(request, 'registration/logout.html')


def Register_View(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=username, password=password1, first_name=first_name,last_name=last_name )
        user.save()
        print('user created')
        return redirect('/accounts/login')
    else:
        return render(request,'registration/register.html')


def Contact_page(request):
    return render(request, 'myapp/contact.html')

def Career_view(request):
    if request.method == 'POST':
        form = JalaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Successfully Completed ')
            return redirect('/')
    else:
        form=forms.JalaForm()
    return render(request, 'myapp/Feedback.html',{'form':JalaForm})