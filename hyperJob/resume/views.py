from django.views import View
# from resume import models
from . import models
from django.shortcuts import render, redirect


class ListResume(View):
    template_name = 'resumeList.html'

    def get(self, request):
        resume = models.Resume.objects.all()
        return render(request, self.template_name, {'resume': resume})


class AddResume(View):
    def post(self, request):
        new_resume = request.POST.get('description')
        if request.user.is_authenticated:
            models.Resume.objects.create(
                description=new_resume, author=request.user
            )
        return redirect('/home/')
