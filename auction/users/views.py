
import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def login_view(request):
    error = None

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.hashedpassword):
                request.session['user_id'] = user.id
                request.session['user_name'] = f"{user.firstname} {user.lastname}"
                return redirect('home')
            else:
                error = 'Неверный email или пароль'
        except User.DoesNotExist:
            error = 'Неверный email или пароль'

    return render(request, 'users/login.html', {'error': error})


def register_view(request):
    error = None

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            error = 'Пользователь с таким email уже существует'
        else:
            hashed_password = make_password(password)
            user = User.objects.create(
                id=str(uuid.uuid4()),
                firstname=firstname,
                lastname=lastname,
                email=email,
                hashedpassword=hashed_password,
                accountbalance=0,
                role=0,
                isblocked=False
            )
            return redirect('login')

    return render(request, 'users/register.html', {'error': error})


def logout_view(request):
    request.session.flush()
    return redirect('login')


















































