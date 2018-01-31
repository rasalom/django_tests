from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    """
    Register form
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        """
        Check email
        """
        check_emails = User.objects.filter(email= self.cleaned_data['email'])
        if check_emails:
            raise ValidationError("A user with email already exist")
        return self.cleaned_data['email']

    def clean_password2(self):
        """
        Check password
        """
        cd = self.cleaned_data

        if len(cd['password']) < 8:
            raise ValidationError("Your password must contain at least 8 characters")

        if cd['password']!=cd['password2']:
            raise ValidationError("Passwords are not the same")
        return cd['password2']

    class Meta:
        model = User
        fields = ['username', 'email']