from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        "page": "Home Page",
        "titles": "Home",
    }

    return render(request, "users/home.html", context)


def register(request):

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        age = request.POST.get('age', '')
        prof_pic = request.FILES.get('profile_picture')

        if password1 == password2:
            user = User.objects.create_user(
                username=username,
                first_name=firstname,
                last_name=lastname,
                password=password1,
                email=email,
                # age=age,
                # profile_picture=prof_pic
            )

            user_prof = UserProfile(
                user=user,
                age=age,
                profile_picture=prof_pic)
            user_prof.save()

        else:
            return render(request, "users/register.html",
                          {'wrong': "Passwords did not match"}
                          )

        return render(request, "users/account.html", {})

    if request.method == 'GET':

        context = {
            "page": "Register Page",
            "titles": "Register",
        }

        return render(request, "users/register.html", context)


def login(request):
    context = {
        "page": "Login Page",
        "titles": "Login",
    }

    return render(request, "users/login.html", context)


@login_required(login_url='/users/login/')
def account(request):
    # user = request.user # get the logged in or registered user information
    # user_profile = User.objects.get(user=request.user)

    context = {
        "page": "Your Account Page",
        "titles": "Account",
    }

    return render(request, "users/account.html", context)


@login_required(login_url='/users/login/')
def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {})
