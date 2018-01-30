from django.shortcuts import render
from django.views.generic.base import TemplateView


class Homepage(TemplateView):
    """
    Homepage 
    """
    template_name = "homepage.html"

