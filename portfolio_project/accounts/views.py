from django.contrib.auth.models import User

from django.contrib.auth.tokens import default_token_generator

from django.core.mail import send_mail

from django.urls import reverse

from django.contrib.sites.shortcuts import get_current_site

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import (
    login,
    logout,
    authenticate
)

from .forms import RegisterForm


# LOGIN
def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            username = form.cleaned_data.get(
                'username'
            )

            password = form.cleaned_data.get(
                'password'
            )

            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                return redirect('/')

    else:

        form = AuthenticationForm()

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


# LOGOUT
def logout_view(request):

    logout(request)

    return redirect('/')


# REGISTO
def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('/')

    else:

        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )

def magic_link_request(request):

    if request.method == 'POST':

        email = request.POST.get('email')

        try:

            user = User.objects.get(email=email)

            token = default_token_generator.make_token(user)

            uid = user.pk

            domain = get_current_site(request).domain

            link = f"http://{domain}/accounts/magic/{uid}/{token}/"

            send_mail(
                'Login mágico',
                f'Clique no link: {link}',
                'admin@portfolio.com',
                [email],
                fail_silently=False,
            )

        except User.DoesNotExist:

            pass

    return render(
        request,
        'accounts/magic_link.html'
    )

def magic_login(request, uid, token):

    try:

        user = User.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):

            login(request, user)

            return redirect('main')

    except User.DoesNotExist:

        pass

    return redirect('login')