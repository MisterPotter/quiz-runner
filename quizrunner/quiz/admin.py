from django.contrib import admin

from .models import Rule, RuleException, Quiz, Question, Answer

admin.site.register(Rule)
admin.site.register(RuleException)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
