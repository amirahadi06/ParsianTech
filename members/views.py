from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('part-add')
        else:
            messages.success(request, "متاسفانه شما مجاز به ورود نمی باشید")
            return redirect('login-user')
    else:
        return render(request, 'members/login_user.html', {})


def logout_user(request):
    logout(request)
    # messages.success(request, "خروج با موفقیت انجام شد")
    return redirect('index')
