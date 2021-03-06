"""hyperjob URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

from main.views import MainMenu, SignupView, UserLoginView
from main.views import AddPost
from resume.views import ListResume, AddResume
from vacancy.views import ListVacancy, AddVacancy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainMenu.as_view()),

    path('resumes/', ListResume.as_view()),
    path('resume/new/', AddResume.as_view()),
    path('resume/new', AddResume.as_view(), name='resume/new'),

    path('vacancies/', ListVacancy.as_view()),
    path('vacancy/new/', AddVacancy.as_view()),
    path('vacancy/new', AddVacancy.as_view(), name='vacancy/new'),

    path('home/', AddPost.as_view()),

    path('signup/', SignupView.as_view()),
    path('signup', SignupView.as_view(), name='signup'),

    path('login/', UserLoginView.as_view()),
    path('login', UserLoginView.as_view(), name='login'),

    path('logout/', LogoutView.as_view()),
    path('logout', LogoutView.as_view(), name='logout'),
]
