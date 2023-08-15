from django import template
from django.utils import timezone


register = template.Library()

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR


@register.filter
def show_date_of_ticket(posted_at):
    seconds_ago = (timezone.now() - posted_at).total_seconds()
    if seconds_ago <= HOUR:
        return f'Publié il y a {int(seconds_ago // MINUTE)} minutes.'
    elif seconds_ago <= DAY:
        return f'Publié il y a {int(seconds_ago // HOUR)} heures.'
    return f'Publié le {posted_at.strftime("%d %B %Y à %Hh%M")}'


@register.filter
def model_type(instance):
    return type(instance).__name__


@register.simple_tag(takes_context=True)
def user_display(context, user):
    if user == context['user']:
        return 'Vous avez'
    return (f"{user.username} a")


@register.simple_tag(takes_context=True)
def username_display(context, user):
    if user == context['user']:
        return 'Vous'
    return (f"{user.username}")
