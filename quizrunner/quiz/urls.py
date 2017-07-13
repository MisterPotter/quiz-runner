from django.conf.urls import url
from quiz.views import RuleList, QuizIndexTemplate, QuizStartView, QuizExceptionView


urlpatterns = [
    url(r'^$', RuleList.as_view(), name='flash_cards'),
    url(r'^quiz/$', QuizIndexTemplate.as_view(), name='quiz_index'),
    url(r'^quiz/exceptions/start/$', QuizStartView.as_view(), name='quiz_exceptions_start'),
    url(
        r'^quiz/exceptions/(?P<quiz_id>[0-9]+)/(?P<question_num>[0-9]+)/$',
        QuizExceptionView.as_view(),
        name='quiz_exceptions'
    )
]
