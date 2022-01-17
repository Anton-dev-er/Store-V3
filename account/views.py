from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from account.forms import RegistrationForm, UserLoginForm


def profile(request):
    return render(request, 'account/user/profile.html')


def account_register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()
            return HttpResponse('registered succesfully and activation sent')
    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': registerForm})


def account_login(request):
    if request.method == 'POST':
        loginForm = UserLoginForm(request.POST)
        password = request.POST['password']
        email = request.POST['email']
        if loginForm.is_valid():
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('account:profile')
            else:
                return HttpResponse('NOT OK')
    else:
        loginForm = UserLoginForm()
    return render(request, 'account/registration/login.html', {'form': loginForm})
