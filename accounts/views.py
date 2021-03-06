from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView

# Create your views here.

class LoginView(TemplateView):
    template_name = 'authentication/login.html'

    def get(self, request):
        return render(request, self.template_name)
