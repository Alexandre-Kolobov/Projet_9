from django import forms
from . import models
# from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model

CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5")
)


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"rows": "5", "class": "form-control"}),
                  }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'headline': forms.TextInput(attrs={"class": "form-control"}),
            'rating': forms.RadioSelect(choices=CHOICES),
            'body': forms.Textarea(attrs={"rows": "5", "class": "form-control"}),
                  }


class FollowUsersForm(forms.ModelForm):
    followers = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Nom d'utilisateur"})
        )
    add_follower = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = get_user_model()
        fields = ["followers"]

    def clean_followers(self):

        follower_username = self.cleaned_data['followers']

        try:
            follower = get_user_model().objects.get(username=follower_username)
        except get_user_model().DoesNotExist:
            raise forms.ValidationError("Cet utilisateur n'existe pas")

        if follower_username == self.instance.username:
            raise forms.ValidationError("Vous ne pouvez pas suivre vous-même")

        if self.instance.following.filter(followed_user__username=follower_username).exists():
            raise forms.ValidationError("Vous suivez déja cet utilisateur")

        return follower.id


class DeleteFollower(forms.Form):
    delete_follower = forms.BooleanField(widget=forms.HiddenInput, initial=True)
