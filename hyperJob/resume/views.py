from django.views import View
from resume import models
from django.shortcuts import render


class ListResume(View):
    template_name = 'resumeList.html'

    def get(self, request):
        resume = models.Resume.objects.all()
        return render(request, self.template_name, {'resume': resume})


