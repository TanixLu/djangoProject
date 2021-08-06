from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            cd = user_login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect('article:article_list')
            else:
                return HttpResponse('用户名或密码错误')
        else:
            return HttpResponse('用户名或密码不合法')
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse('请使用POST或GET方式请求')


def user_logout(request):
    logout(request)
    return redirect('article:article_list')
