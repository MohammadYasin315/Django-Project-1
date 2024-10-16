from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm, UserLoginform
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def user_rgeister(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'ٍثبت نام شما موفقیت آمیز بود', 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, ('rgeister.html'), ({'form':form}))



def user_login(request):
    if request.method == 'POST':
        form = UserLoginform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                login(request, user) 
                messages.success(request, 'ورود شما موفقیت آمیز بود', 'success')
                return redirect('home')
            else:
                messages.error(request, 'نام کاربری و رمز شما اشتباه است', 'danger')
    else:
        form = UserLoginform()
    return render(request, ('login.html'), ({'form':form}))

def user_logout(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید', 'success')
    return redirect('home')