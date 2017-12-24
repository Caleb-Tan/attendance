"""attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import django.contrib.auth.views as auth_views
from attendanceapp import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='Index'),
	url(r'^login/$', auth_views.login, name="login"),
	url(r'^logout/$', auth_views.logout, name="logout"),
    url(r'^scanCard/$', views.logInPage, name='scanCard'),
    url(r'^viewPeopleInfo/$',views.viewPeopleInfo,name="viewPeopleInfo"),
	url(r'^leaderboard/$',views.leaderboard, name="leaderboard"),
    url(r'^viewPeopleStats/$', views.viewPeopleStats, name="viewPeopleStats"),
    url(r'^viewSubteamStats/$', views.viewSubteamStats, name="viewSubteamStats"),
]