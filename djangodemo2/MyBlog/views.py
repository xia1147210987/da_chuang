# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.http import HttpResponse
import os
import json
from django.shortcuts import HttpResponse, render, redirect
from django.views.decorators.csrf import csrf_exempt

from django.urls import reverse
from MyBlog.form import RegisterForm, LoginForm, Postopic, prPostopic
from MyBlog.models import UserProfile, topic, reply, prtopic

"""
    视图函数
"""

def home(request):
    """
    返回论坛首页
    """
    return render(request, 'main.html')

def index(request):
    """
    返回登录/注册界面
    """
    return render(request, 'index.html')

def Topic(request):
    """
    返回帖界面
    """
    return render(request, 'Topic.html')

def Send(request):
    """
    发帖界面
    """
    return render(request, 'pustopic.html')

def prSend(request):
    """
    发隐私帖界面
    """
    return render(request, 'pripustopic.html')

def prmain(request):
    """
    隐私帖界面
    """
    return render(request, 'primain.html')

# 用户注册
def user_register(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        rform = RegisterForm(request.POST)  # 使用form获取数据
        print('--------》', rform)
        print("errors", rform.errors)
        if rform.is_valid():  # 进行数据的校验
            # 从通过前端校验的数据中取值
            username = rform.cleaned_data.get('username')
            password = rform.cleaned_data.get('password')
            # 如果用户名不存在的话，才进行添加数据操作
            if not UserProfile.objects.filter(Q(username=username)).exists():
                # 注册到数据库中
                password = make_password(password)  # 加密密码
                id = abs(hash(username)) % (10 ** 8)   #生成id
                user = UserProfile.objects.create(username=username, password=password, id=id)
                if user:
                    # 如果用户创建成功，则提示注册成功,返回tip等于1，弹出成功提示窗口
                    return render(request, 'index.html', context={'msg': '注册成功', 'tip': 1})
            else:
                # 如果用户名存在，返回tip等于2，弹出失败提示窗口
                return render(request, 'index.html', context={'msg': '用户名已经存在！', 'tip': 2})
        # 数据校验失败，提示注册失败
        return render(request, 'index.html', context={'msg': '用户名已经存在，请重新填写！', 'tip': 2})

# 用户登录
def user_login(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        lform = LoginForm(request.POST)
        print('--------》', lform)
        print("errors", lform.errors)
        if lform.is_valid():
            username = lform.cleaned_data.get('username')
            password = lform.cleaned_data.get('password')
            # 查询数据库,如果加密后的两个密码一致的话登录成功
            # 用户数据
            user = UserProfile.objects.filter(username=username).first()
            flag = check_password(password, user.password)
            # 论坛帖数据
            topics = list(topic.objects.all())
            if flag:
                # 登陆成功后，保存session信息，获取用户和论坛的数据，并进入首页
                # session信息会保存到django_session表中，并进行base64加密
                user = {'uname': user.username, 'UID': user.id}
                # request.session['username'] = username
                # topics['uname'] = username
                # topics['UID'] = id
                infornation = {'topics': topics, 'user': user}
                return render(request, 'main.html', {'infornation': infornation})
                # return redirect(reverse('home'))
        return render(request, 'index.html', context={'errors': lform.errors})


def user_logout(request):
    """
    用户注销
    """
    # 方法一、可自行清空session，再重定向到首页
    # request.session.clear() # 仅删除字典
    # 用户注销后，把session给清空，并且重定向回首页
    # request.session.flush()  # 删除django_session +cookie + 字典
    # return redirect(reverse('index'))

    # 方法二、若model类继承了AbstractUser，可直接使用系统自带的退出登录，即logout；不需要自己去清空session
    logout(request)
    return redirect(reverse('index'))

# 用户发帖
def user_postopic(request):
    # 使用form获取数据
    rform = Postopic(request.POST)
    if request.method == 'GET':
        return render(request, 'main.html')
    else:
        print('--------》', rform)
        print("errors：", rform.errors)
        # if rform.is_valid():  # 进行数据的校验
        # 从通过前端校验的数据中取值
        title = rform.cleaned_data.get('TTopic')
        message = rform.cleaned_data.get('TContent')
        uid = int(rform.cleaned_data.get('UID'))
        # 获取用户信息
        userinf = UserProfile.objects.filter(id=uid).first()
        # 注册到数据库中
        user = topic.objects.create(TTopic=title, TContent=message, UID_id=userinf.id, username=userinf.username)
        if user:
            # 如果成功
            topics = list(topic.objects.all())
            user = {'uname': userinf.username, 'UID': userinf.id}
            infornation = {'topics': topics, 'user': user}
            return render(request, 'main.html', {'infornation': infornation})
        else:
            # 如果失败
            return HttpResponse("保存失败！")
            # return render(request, 'main.html', context={'msg': '发帖失败！', 'tip': 2})
        # 失败
        # return HttpResponse("发帖失败！")
        # return render(request, 'main.html', context={'msg': '发帖失败！', 'tip': 2})

# 用户发隐私帖
def prpostopic(request):
    # 使用form获取数据
    rform = prPostopic(request.POST)
    if request.method == 'GET':
        return render(request, 'main.html')
    else:
        print('--------》', rform)
        print("errors", rform.errors)
        if rform.is_valid():  # 进行数据的校验
            # 从通过前端校验的数据中取值
            title = rform.cleaned_data.get('TTopic')
            message = rform.cleaned_data.get('TContent')
            uid = int(rform.cleaned_data.get('UID'))
            # 获取用户信息
            userinf = UserProfile.objects.filter(id=uid).first()
            # 注册到数据库中
            if rform.cleaned_data.get('rid') == None:
                user = prtopic.objects.create(TTopic=title, TContent=message, UID_id=uid, username=userinf.username)
            else:
                rid = int(rform.cleaned_data.get('rid'))
                user = prtopic.objects.create(TTopic=title, TContent=message, UID_id=uid, username=userinf.username,
                                              reid=rid)
            if user:
                # 如果成功
                topics = list(topic.objects.all())
                user = {'uname': userinf.username, 'UID': userinf.id}
                infornation = {'topics': topics, 'user': user}
                return render(request, 'main.html', {'infornation': infornation})
            else:
                # 如果失败
                return HttpResponse("保存失败！")
                # return render(request, 'main.html', context={'msg': '发帖失败！', 'tip': 2})
        # 失败
        return HttpResponse("发帖失败！")
        # return render(request, 'main.html', context={'msg': '发帖失败！', 'tip': 2})

# 用户访问隐私帖界面
@csrf_exempt
def save_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        return HttpResponse({username})
    else:
        return render(request, 'index.html')

def get_user(request):
    if request.method == "POST":
        uname = request.POST.get("uid")
        userinf = UserProfile.objects.filter(username=uname).first()
        print(userinf)
        return HttpResponse({userinf.id})
    else:
        return render(request, 'index.html')

def process_url_from_client(request):
    # urls = request.POST.get('url')
    # print(urls)
    response = json.dumps({
        'status': 'ok',
    })
    return render(request, 'primain.html')


def getTopic(info):
    print(info)
    TIDs = info['TID']
    Topic = topic.objects.filter(TID=TIDs).first()
    replys = reply.objects.filter(TID=TIDs)
    inf = {'Topic': Topic, 'uid': info['uid'], 'replys': replys}
    return inf

#获取主贴信息
def get_topic(request):
    if request.method == "POST":
        TID = int(request.POST.get("TID"))
        uid = request.POST.get("UID")
        Topic = topic.objects.filter(TID=TID).first()
        replys = reply.objects.filter(TID=TID)
        inf = {'Topic': Topic, 'uid': uid, 'replys': replys}
        return render(request, 'Topic.html', {'inf': inf})
    else:
        return render(request, 'index.html')

# 发布回复帖
def postreply(request):
    if request.method == "POST":
        rcontent = request.POST.get("rcontent")
        TID = int(request.POST.get("TID"))
        Uid_id = int(request.POST.get("ruid"))
        print(Uid_id)
        username = UserProfile.objects.filter(id=Uid_id).first().username
        replys = reply.objects.create(TID=TID, UID_id=Uid_id, RContent=rcontent, username=username)
        if replys:
            info = {'TID': TID, 'uid': Uid_id}
            inf = getTopic(info)
            return render(request, 'Topic.html', {'inf': inf})
        else:
            return render(request, 'index.html')

def gmain(request):
    uname = request.POST.get("uname")
    user = UserProfile.objects.filter(username=uname).first()
    topics = list(topic.objects.all())
    user = {'uname': user.username, 'UID': user.id}
    infornation = {'topics': topics, 'user': user}
    return render(request, 'main.html', {'infornation': infornation})

# 获得隐私帖的列表
def gprmain(request):
    uname = request.POST.get("uname")
    user = UserProfile.objects.filter(username=uname).first()
    uid = user.id
    only = list(prtopic.objects.filter(reid=uid))
    ran = list(prtopic.objects.filter(reid=None))
    # topics = list(prtopic.objects.all())
    user = {'uname': user.username, 'UID': user.id}
    infornation = {'topics': only, 'user': user, 'ran': ran}
    return render(request, 'primain.html', {'infornation': infornation})
# 获得隐私帖
def prgetopic(request):
    if request.method == "POST":
        TID = int(request.POST.get("TID"))
        uid = request.POST.get("UID")
        if prtopic.objects.filter(Q(TID=TID)).exists():
            Topic = prtopic.objects.filter(TID=TID).first()
            inf = {'Topic': Topic, 'uid': uid}
            prtopic.objects.get(TID=TID).delete()
            return render(request, 'prTopic.html', {'inf': inf})
        else:
            user = UserProfile.objects.filter(id=uid).first()
            topics = list(prtopic.objects.all())
            infornation = {'topics': topics, 'user': user}
            return render(request, 'primain.html', {'infornation': infornation})
    else:
        return render(request, 'index.html')