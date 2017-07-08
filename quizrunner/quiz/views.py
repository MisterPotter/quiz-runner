from django.shortcuts import render

from material import Layout, Row, Fieldset
from material.frontend.views import ModelViewSet

from .models import RuleException


def index(request):
    return render(request, 'quiz/index.html')


def exceptions(request):
    return render(request, 'quiz/exceptions.html')
