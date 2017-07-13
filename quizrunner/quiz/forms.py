from django.forms import ChoiceField, Form, RadioSelect

from quiz.models import RuleException, Question


class QuizQuestionForm(Form):
    class Meta:
        model = RuleException

    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop('quiz', None)
        num = int(kwargs.pop('num', None))
        super().__init__(*args, **kwargs)

        questions = list(Question.objects.filter(quiz=quiz))
        question = questions[num]
        answers = (question.answer_set.all())
        self.fields['select'] = ChoiceField(
            label='Question x:...',
            widget=RadioSelect,
            choices=[(answer.correct, answer.exception.description) for answer in answers]
        )
