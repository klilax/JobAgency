from django.views import View
from . import models
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden


class ListVacancy(View):
    template_name = 'vacancyList.html'

    def get(self, request):
        vacancy = models.Vacancy.objects.all()
        return render(request, self.template_name, {'vacancy': vacancy})


class AddVacancy(View):
    def post(self, request):
        new_resume = request.POST.get('description')
        if request.user.is_staff:
            models.Vacancy.objects.create(
                description=new_resume, author=request.user
            )
            return redirect('/home/')
        else:
            return HttpResponseForbidden()
