from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from .models import Profile
from.forms import RegisterForm


class RegisterView(FormView):
    """
    Register view
    """
    form_class = RegisterForm
    template_name = "register.html"

    def form_valid(self, form):

        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()

        Profile.objects.create(user = new_user)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pages:homepage')


class ProfileView(TemplateView):
    """
    Profile show
    """
    template_name = 'profile.html'


