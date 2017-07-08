from django.conf.urls import url

from quiz.views import RuleList


urlpatterns = [
    url(r'^$', RuleList.as_view(), name='flash_cards'),
]
