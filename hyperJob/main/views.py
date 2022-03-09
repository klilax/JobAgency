from django.shortcuts import render
from django.views import View


class MainMenu(View):
    template_name = 'main.html'

    def get(self, request):
        return render(request, self.template_name)
