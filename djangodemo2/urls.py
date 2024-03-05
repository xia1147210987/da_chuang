"""djangoDemo2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  form.py my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  form.py other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: form.py django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyBlog import views

from django.conf.urls.static import static
from django.conf import settings
from MyBlog.views import user_register, user_login, user_logout, user_postopic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('', views.index),
    path('home/', views.topic, name='home'),
    path('register', user_register, name='register'),
    path('login', user_login, name='login'),
    path('pmain/', views.prmain),
    path('postopic', user_postopic, name='postopic'),
    path('prpostopic/', views.prpostopic, name='prpostopic'),
    path('logout', user_logout, name='logout'),
    path('send/', views.Send, name='send'),
    path('prsend/', views.prSend, name='prsend'),
    path('userinf/', views.save_view),
    path('pmain/getuser/', views.get_user),
    path('getopic', views.get_topic, name='getopic'),
    path('postre',views.postreply, name='postre'),
    path('gmain', views.gmain, name='gmain'),
    path('gprmain', views.gprmain, name='gprmain'),
    path('prgetopic', views.prgetopic, name='prgetopic'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

