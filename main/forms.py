from typing import Any

from django import forms

from .models import User


def get_role_choices() -> list[tuple[int, str], tuple[int, str], tuple[int, str]]:
    role_choices = User.RoleChoices.choices
    role_choices.pop(2)
    return role_choices


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'id': 'password'}
        )
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(
            attrs={
                'id': 'confirm_password'
            }
        )
    )
    other_country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'other_country',
                'style': 'display: none',
                'placeholder': 'Enter country'
            }
        ),
        required=False
    )
    other_nationality = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'other_nationality',
                'style': 'display: none',
                'placeholder': 'Enter nationality'
            }
        ),
        required=False
    )
    role = forms.ChoiceField(choices=get_role_choices())

    class Meta:
        model = User
        fields = (
            'full_name', 'mobile', 'email', 'country', 'role',
            'nationality', 'other_country', 'other_nationality'
        )
        widgets = {
            'email': forms.EmailInput(attrs={'id': 'email'}),
            'mobile': forms.TextInput(attrs={'id': 'mobile', 'type': 'tel'}),
            'country': forms.Select(attrs={'id': 'country', 'onchange': 'checkOther(this)'}),
            'nationality': forms.Select(attrs={'id': 'nationality', 'onchange': 'checkOther(this)'}),
            'full_name': forms.TextInput(attrs={'id': 'fullName'})
        }

    def clean_mobile(self):
        mobile: str = self.cleaned_data.get('mobile', '')
        if mobile.isdigit():
            return mobile
        raise forms.ValidationError('Invalid mobile number')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, *args, **kwargs) -> Any:
        self.cleaned_data.pop('password2', '')
        user: User = User.objects.create_user(**self.cleaned_data)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
