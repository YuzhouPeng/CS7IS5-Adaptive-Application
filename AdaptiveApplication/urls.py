"""AdaptiveApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import *
from adaptive_dashboard import views as adaptive_dashboard_views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('home/', adaptive_dashboard_views.home, name='home'),
    path('contact/', adaptive_dashboard_views.contact, name='contact'),
    path('login/', adaptive_dashboard_views.login, name='login'),
    path('register/',adaptive_dashboard_views.register, name='register'),
    path('index/', adaptive_dashboard_views.index, name='index'),
    path('monitor/', adaptive_dashboard_views.monitor, name='monitor'),
    path('logout/', adaptive_dashboard_views.logout, name='logout'),
    path('dashboard/', adaptive_dashboard_views.dashboard, name='dashboard'),

]
