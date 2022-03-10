from django.views import View
from vacancy import models
from django.shortcuts import render


class ListVacancy(View):
    template_name = 'vacancyList.html'

    def get(self, request):
        vacancy = models.Vacancy.objects.all()
        return render(request, self.template_name, {'vacancy': vacancy})


