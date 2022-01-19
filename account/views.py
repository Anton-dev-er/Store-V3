from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str


from account.forms import RegistrationForm, UserLoginForm
from account.models import UserBase
from account.token import account_activation_token


def profile(request):
    return render(request, 'account/user/profile.html')


def account_register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = registerForm.cleaned_data.get('email')
            send_mail(subject=subject,
                      message=message,
                      from_email='from_email@gmail.com',
                      recipient_list=to_email,
                      fail_silently=False)
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


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except():
        pass

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:profile')
    else:
        return render(request, 'account/registration/activation_invalid.html')