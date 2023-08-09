from django import forms
from . import models
# from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model

CHOICES = (
    (1,"1"),
    (2,"2"),
    (3,"3"),
    (4,"4"),
    (5,"5")
)

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={"rows":"5","class": "form-control"}),
            'description': forms.Textarea(attrs={"rows":"5","class": "form-control"}),
                  }
    
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'headline': forms.TextInput(attrs={"rows":"5","class": "form-control"}),
            'rating': forms.RadioSelect(choices=CHOICES),
            'body': forms.Textarea(attrs={"rows":"5","class": "form-control"}),
                  }
