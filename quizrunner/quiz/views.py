from django.shortcuts import get_object_or_404
from django.views.generic import FormView, ListView, RedirectView, TemplateView
from random import shuffle

from .forms import QuizQuestionForm
from .models import Answer, Rule, RuleException, Question, Quiz
from .types import QuestionStatus


class RuleList(ListView):
    queryset = Rule.objects.all()
    context_object_name = 'rule_list'
    template_name = 'quiz/rule_list.html'


class QuizIndexTemplate(TemplateView):
    template_name = 'quiz/quiz_index.html'


class QuizStartView(RedirectView):
    permanent = False
    query_string = False
    pattern_name = 'quiz_exceptions'

    def get_redirect_url(self, *args, **kwargs):
        quiz_id = self._generate_quiz()
        kwargs['quiz_id'] = quiz_id
        kwargs['question_num'] = 1
        return super().get_redirect_url(*args, **kwargs)

    def _generate_quiz(self):
        quiz = Quiz()
        quiz.save()

        rule_exception_list = list(RuleException.objects.all())
        shuffle(rule_exception_list)
        rule_exception_list_copy = rule_exception_list[:]

        for _ in range(len(rule_exception_list)):
            question = Question(status=QuestionStatus.UNANSWERED.value, quiz=quiz)
            question.save()

            correct_answer = rule_exception_list.pop(0)
            correct_answer_object = Answer(
                correct=True,
                picked=False,
                exception=correct_answer,
                question=question
            )
            correct_answer_object.save()

            wrong_answer_list = rule_exception_list_copy[:]
            wrong_answer_list.remove(correct_answer)
            shuffle(wrong_answer_list)

            for _ in range(0, 3):
                wrong_answer = wrong_answer_list.pop()
                wrong__answer_object = Answer(
                    correct=True,
                    picked=False,
                    exception=wrong_answer,
                    question=question
                )
                wrong__answer_object.save()

        return quiz.id


class QuizExceptionView(FormView):
    template_name = 'quiz/quiz_exception.html'
    form_class = QuizQuestionForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.quiz = get_object_or_404(Quiz, pk=kwargs['quiz_id'])
        self.question_num = kwargs['question_num']
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return dict(kwargs, quiz=self.quiz, num=self.question_num)

    def form_valid(self, form):
        pass

    def form_invalid(self, form):
        pass
