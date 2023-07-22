from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from authentication.forms import CreateUserForm

from . import forms

class LoginPageView(View):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})

def logout_user(request):
    logout(request)
    return redirect('login')

def create_user(request):
    form = CreateUserForm()
    return render(request,
        'authentication/user_create.html',
        {'form': form})

class CreateUserView(View):
    form_class = forms.CreateUserForm
    template_name = 'authentication/user_create.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, context={'form': form})