from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.shortcuts import redirect
from adaptive_dashboard import models
from adaptive_dashboard import form
import hashlib
from django.http import HttpResponseServerError, HttpResponse
import json
import operator
# from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
# from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def get_adaptive_keywords(user_id, topic_id, page_id):
    user_topic, created = models.UserTopic.objects.get_or_create(
        topic_id=topic_id,
        user_id=user_id, defaults={
            'total_count': 0,
            'last_page_count': 0,
            'last_page_id_of_topic': 0})

    update_user_topic(user_topic)

    keywords = models.Keywords.objects.filter(page_id=page_id, start_index__isnull=False).order_by('-similarity')
    num_keywords = len(keywords)

    ret_num = int(num_keywords * user_topic.topic_score)
    keyfun = operator.attrgetter('start_index')
    filtered_keywords = keywords[:ret_num]
    # filtered_keywords.sort(key=lambda x: x.start_index)
    new_filtered_keywords = sorted(filtered_keywords, key=keyfun)
    return new_filtered_keywords


def cal_score(t_scr, k):
    if (t_scr <= 0.11 and k == 0) or k == 1:
        return t_scr
    if 2 <= k <= 4:
        a = 0.6
    elif k >= 5:
        a = 0.2
    else:
        a = 1.5
    score = (pow(a, t_scr) - 1) / (a - 1)
    return score


def update_user_topic(user_topic):
    if user_topic.last_page_id_of_topic != 0:
        updated_topic_score = cal_score(user_topic.topic_score, user_topic.last_page_count)
        user_topic.topic_score = updated_topic_score
        user_topic.save()


def page_change(request):
    if request.is_ajax() and request.method == 'GET':
        last_page_id = int(request.GET.get('last-page', None))
        topic_id = request.GET.get('topic', None)
        if request.session.get('is_login', None):
            user_id = request.session['user_id']

        # all_user_topics = models.UserTopic.objects.filter(user_id=user_id)
        # for all_user_topic in all_user_topics:
        #     all_user_topic.last_page_id = last_page_id
        #     all_user_topic.save()

        user_topic = models.UserTopic.objects.get(topic_id=topic_id, user_id=user_id)
        # if user_topic.last_page_id_of_topic != last_page_id:
        #     user_topic.last_page_count = 0
        #     update_user_topic(user_topic)
        user_topic.last_page_id_of_topic = last_page_id
        if user_topic.model_updated == 0:
            user_topic.last_page_count = 0
            user_topic.save()

        new_page_id = int(request.GET.get('new-page', None))
        user = models.User.objects.get(id = user_id)
        user.last_visited_page = new_page_id
        user.save()
        request.session['current_page'] = '/wikipage/' + str(new_page_id)
        new_page_topic_id = models.Page.objects.get(id=new_page_id).topics_id

        new_user_topic = models.UserTopic.objects.get(topic_id=new_page_topic_id, user_id=user_id)
        new_user_topic.model_updated = 0
        new_user_topic.last_page_count = 0
        new_user_topic.save()

        return HttpResponse(json.dumps({"status": "page change event noted."}))


def model_update(request):
    if request.is_ajax() and request.method == 'GET':
        topic_id = request.GET.get('topic', None)
        page_id = int(request.GET.get('page', None))
        if request.session.get('is_login', None):
            user_id = request.session['user_id']
            user_topic, created = models.UserTopic.objects.get_or_create(
                topic_id=topic_id,
                user_id=user_id, defaults= {
                    'total_count': 0,
                    'last_page_count': 0,
                    'last_page_id_of_topic': 0})
            user_topic.total_count = user_topic.total_count + 1
            # if page_id != user_topic.last_page_id_of_topic:
            #     user_topic.last_page_count = 0
            user_topic.last_page_id_of_topic = page_id
            user_topic.model_updated = 1
            user_topic.last_page_count += 1
            user_topic.save()
        else:
            return redirect('/login/')

        return HttpResponse(json.dumps({"status": "model will remember this..."}))


def wikipage(request, pageid):
    page_id = pageid

    page = models.Page.objects.get(id = page_id)
    if request.session.get('is_login', None):
        user_id = request.session['user_id']
    else:
        return redirect('/login/')

    keywords = get_adaptive_keywords(user_id=user_id, topic_id=page.topics_id, page_id=page_id)
    total_keywords = models.Keywords.objects.filter(page_id=page_id).count()
    shown_keywords = len(keywords)
    keywords_list = list()
    for keyword in keywords:
        retKey = {
            "name": keyword.name,
            "start_index": keyword.start_index,
            "end_index": keyword.end_index,
            "similarity": keyword.similarity,
            "summary": keyword.summary,
        }
        keywords_list.append(retKey)
    return render(request, 'wiki-page.html', { "page": json.dumps(model_to_dict(page)),"keywords": json.dumps(keywords_list), 'page_id':page_id, "shown_len": shown_keywords,
            "total_len":total_keywords})


def dashboard(request):
    if request.method == "POST":
        # register_form = form.Dashboard(request.POST)
        topics = request.POST.getlist('someSwitchOption001')
        # username = request.session['user_id']
        all_topics = models.Topics.objects.all()
        if request.session.get('is_login', None) is not None:
            if request.session['is_login'] == True:
                user_id = request.session['user_id']
                for topic in all_topics:
                    user_topic, created = models.UserTopic.objects.get_or_create(
                        topic_id=topic.id,
                        user_id=user_id, defaults={
                            'total_count': 0,
                            'last_page_count': 0,
                            'last_page_id_of_topic': 0})
                    if str(topic.id) in topics:
                        user_topic.topic_score = 0.75
                    else:
                        user_topic.topic_score = 0.5
                    user_topic.last_page_id_of_topic = 0
                    user_topic.save()

            return redirect(request.session['current_page'])
            # return redirect('/wikipage/1/')

    return render(request, 'dashboard.html')


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
        return redirect("/dashboard/")
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
                    request.session['user_name'] = user.name.capitalize()
                    request.session['user_page_id'] = 1
                    request.session['current_page'] = '/wikipage/' + str(user.last_visited_page)
                    if user.new_user == 1:
                        user.new_user = 0
                        user.save()
                        return redirect('/dashboard/')
                    else:
                        request.session['current_page'] = '/wikipage/' + str(user.last_visited_page)
                        return redirect('/index/')
                        # ret_page = '/wikipage/' + str(user.last_visited_page)
                        # return redirect(ret_page)
                    # return redirect('/wikipage/1')
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