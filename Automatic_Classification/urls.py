"""Automatic_Classification URL Configuration

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


from django.contrib import admin
from django.urls import path
from user_profile.views import (login_view,home_page_view,feedback_view)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_view,name='login'),
    path('<str:zone>/',feedback_view,name='feedback-1'),
    path('',home_page_view,name='home_page')
    ]

