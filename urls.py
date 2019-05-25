"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^fetch_k', csrf_exempt(get_k), name='get_k'),
    url(r'^get_codes_count', csrf_exempt(get_count), name='get_count'),
    url(r'^get_events', csrf_exempt(get_events), name='get_events'),
    url(r'^get_comments', csrf_exempt(get_comments), name='get_comments'),
    url(r'^get_stock_list', csrf_exempt(get_stock_list), name='get_stock_list'),

]
