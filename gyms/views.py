from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from gyms.forms import AdminSignUpForm
from gyms.models import User

class AdminSignUp(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/admin_home/')

def AdminHome(request):
    return render(request, 'admin_home.html')
