from django.contrib import admin

from .models import Rule, RuleException

admin.site.register(Rule)
admin.site.register(RuleException)
