from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreateForm(UserCreationForm):

    username = forms.CharField(
        label="username",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete':'usename',
            "type": "text",
            "placeholder": "Entrer le nom d'utilisateur"

        }),
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete':'new-password',
            "type": "password",
            "placeholder": "Entrer le motdepasse"

        }),
    )
    password2 = forms.CharField(
        label="Confirm password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete':'new-password',
            "type": "password",
            "placeholder": "Entrer le motdepasse"

        }),
    )

    # password2 = forms.CharField(
    #     label="Confirm password",
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
    # )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")