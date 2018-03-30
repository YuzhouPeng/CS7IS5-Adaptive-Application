from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.shortcuts import redirect
from adaptive_dashboard import models
from adaptive_dashboard import form
from django.contrib import sessions
import hashlib
from django.http import HttpResponseServerError
import json
# from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
# from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

#@login_required(login_url='/login')
#@cache_page(CACHE_TTL)
def wikipage(request):
    page = models.Page.objects.get(id = 1)
    return render(request, 'wiki-page.html', {
        "page": json.dumps(model_to_dict(page))
    })


def index(request):
    return render(request, 'index.html')
def test(request):
    return render(request, 'test.html')

def register(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        register_form = form.RegisterForm(request.POST)
        message = "Please check the input"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = "Input of two password is different!"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = 'User existed, please choose a new username'
                    return render(request, 'register.html', locals())
                same_name_user = models.User.objects.filter(email=email)
                if same_name_user:
                    message = 'The email has been registered, please use other email'
                    return render(request,'register.html',locals())
                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')
    register_form = form.RegisterForm()
    return render(request, 'register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    request.session.flush()
    return redirect('/index/')

def home(request):
    pass
    return render(request, 'index.html')

def contact(request):
    pass
    return render(request, 'contact.html')

def monitor(request):
    pass
    return render(request, 'monitor.html')

def login(request):
    #send_mail('subject', 'message', 'pengyuzhou2017@sina.com', ['pengyuzhou760783896@gmail.com'], fail_silently=False)
    if request.session.get('is_login',None):
        return redirect("/index/")
    #test error 500
    #test_error_500_view()
    if request.method == "POST":
        login_form = form.UserForm(request.POST)
        message = "Please check the imput of username/password"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "Password incorrect"
            except:
                message = "Non-exist user"
        return render(request, 'login.html', locals())

    login_form = form.UserForm()
    return render(request, 'login.html', locals())

def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()
# test sending email

def test_error_500_view(request):
    return HttpResponseServerError()