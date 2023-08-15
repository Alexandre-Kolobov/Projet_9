from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Nom d'utilisateur"}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Mot de passe"}))


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        max_length=63,
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nom d'utilisateur"}))
    password1 = forms.CharField(
        max_length=63,
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Mot de passe"}))
    password2 = forms.CharField(
        max_length=63,
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirmer le mot de passe"}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Ancien mot de passe"})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Nouveau mot de passe"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirmation du nouveau mot de passe"})
