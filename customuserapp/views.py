from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
# from django.db import models
from customuserapp.models import MyUser
from customuserapp.forms import LogInForm, NewCustomUser
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django_customUser.settings import AUTH_USER_MODEL

# Create your views here.


# @login_required
def home_page(request):
    html = "home_page.html"
    content = AUTH_USER_MODEL
    if request.user.is_authenticated:
        return render(request, html, {'content': content})
    return redirect('/login/')



def login_view(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage')))

    form = LogInForm()
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
        

def newuser_view(request):
    if request.method == 'POST':
        form = NewCustomUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email']
            )
            new_user = MyUser.objects.last()
            new_user.set_password("")
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage')))
        return render(request, "newuser_form.html", {"form": form})
    form = NewCustomUser()
    return render(request, "newuser_form.html", {"form": form})

            