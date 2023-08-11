from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from . import models
from authentication import models as auth_models
from . import forms
from django.shortcuts import get_object_or_404
from itertools import chain


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    tickets_and_reviews = sorted(chain(tickets, reviews), key=lambda instance: instance.date_created, reverse=True)
    return render(request, 'blog/home.html', context={'tickets_and_reviews': tickets_and_reviews})

@login_required
def ask_review(request):
    template_name = 'blog/ask_review.html'
    form = forms.TicketForm()

    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form_to_save = form.save(commit=False)
            form_to_save.user = request.user
            form_to_save.save()
            return redirect('home')
    return render(request, template_name, context={'form': form})

@login_required
def view_show_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'blog/view_show_ticket.html', {'ticket': ticket})

@login_required
def view_create_ticket_and_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    
    context ={
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'blog/view_create_ticket_and_review.html', context=context)

@login_required
def view_create_review(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review_form = forms.ReviewForm()

    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')

    context ={
        'ticket': ticket,
        'review_form': review_form,
    }
    return render(request, 'blog/view_create_review.html', context=context)

@login_required
def show_flux(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)
    tickets_and_reviews = sorted(chain(tickets, reviews), key=lambda instance: instance.date_created, reverse=True)
    return render(request, 'blog/flux.html', context={'tickets_and_reviews': tickets_and_reviews})


@login_required
def follow_users(request):

    users = auth_models.User.objects.exclude(username=request.user)
    form_add = forms.FollowUsersForm(instance=request.user, initial={'followers': ''})
    form_delete = forms.DeleteFollower()
    following = request.user.following.all()
    followed_by = request.user.followed_by.all()

    if request.method == 'POST':
        if "add_follower" in request.POST:
            form_add = forms.FollowUsersForm(request.POST, instance=request.user)
            if form_add.is_valid():
                follower_to_add = auth_models.User.objects.get(username=request.POST.get("followers"))
                request.user.followers.add(follower_to_add)
                return redirect('followers')
            
        if "delete_follower" in request.POST:
            form_delete = forms.DeleteFollower()
            print(request.POST)
            if form_delete.is_valid():
                follower_to_delet = auth_models.User.objects.get(username=request.POST.get("followers"))
                request.user.followers.remove(follower_to_delet)
                return redirect('followers')
    
    context ={
        'form_add': form_add,
        'form_delete': form_delete,
        'users':users,
        'following':following,
        'followed_by':followed_by,
        'user':request.user
    }
    return render(request, 'blog/followers.html', context=context)
