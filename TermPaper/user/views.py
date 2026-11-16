from django.shortcuts import render, redirect
from .models import User
from .forms import LoginForm, JoinForm


def login(request):
    error = ''
    database = User.objects.all()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password'] 
            for user in database:
                if user.login == login and user.password == password:
                    request.session['user_first'] = user.first_name
                    request.session['user_last'] = user.last_name
                    request.session['user_login'] = user.login
                    request.session['user_admin'] = user.admin
                    return redirect('home')
                else:
                    error = 'Не вірний логін або пароль!'

    else:
        form = LoginForm()

    data = {
        'form': form,
        'error': error,
        'database': database,
    }
    return render(request, 'user/login.html', data)

def logout(request):
    request.session.flush()
    return redirect('home')

def join(request):
    error = ''
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма була некоректна!'

    form = JoinForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'user/join.html', data)
