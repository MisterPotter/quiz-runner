from django.shortcuts import render
from django.views.generic import ListView

from material import Layout, Row, Fieldset
from material.frontend.views import ModelViewSet

from .models import Rule, RuleException


class RuleList(ListView):
    queryset = Rule.objects.all()
    context_object_name = 'rule_list'
    template_name = 'quiz/rule_list.html'
