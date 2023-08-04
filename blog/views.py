from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from . import forms

@login_required
def home(request):
    return render(request, 'blog/home.html')

@login_required
def ticket_creation(request):
    template_name = 'blog/ticket_creation.html'
    form = forms.TicketForm()

    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form_to_save = form.save(commit=False)
            form_to_save.user = request.user
            form_to_save.save()
            return redirect('home')
    return render(request, template_name, context={'form': form})
