from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

from .types import QuestionStatus


class Rule(models.Model):
    """A rule which specifies some rules to be followed.

    :param name: The name of the rule.
    :type name: str

    :param description: A longer description used for the rule,
        it will be used in tests to determine the rule.
    :type description: str
    """
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300)

    def __str__(self):
        return '({name}, {description})'.format(
            name=self.name,
            description=self.description
        )


class RuleException(models.Model):
    """An exception which breaks a rule.

    :param name: The name of the exception.
    :type name: str

    :param description: A longer description used for the exception,
        it will be used in tests to determine the exception.
    :type description: str

    :param rule: The rule that is being broken by the exception.
        If the rule is deleted, remove the exceptions.
    :type rule: Rule
    """
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)

    def __str__(self):
        return '({name}, {description}, {rule})'.format(
            name=self.name,
            description=self.description,
            rule=self.rule.name
        )


class Quiz(models.Model):
    """A quiz to score a user based on their knowledge of rules and exceptions.

    """
    creation_date = models.DateTimeField('date created')

    def __str__(self):
        '({date})'.format(date=self.creation_date)

    @property
    def done(self):
        return True


class Question(models.Model):
    STATUS_CHOICES = (
        (QuestionStatus.UNANSWERED, 'unanswered'),
        (QuestionStatus.RIGHT, 'right'),
        (QuestionStatus.WRONG, 'wrong'),
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=QuestionStatus.UNANSWERED
    )
    quiz = models.ForeignKey(Quiz)


class Answer(models.Model):
    """An answer to a question.

    An answer can be a text from a Rule OR RuleException, even within
    the same quiz.
    """
    correct = models.BooleanField(default=False)
    picked = models.BooleanField(default=False)

    limit = models.Q(app_label='quiz', model='rule') | \
        models.Q(app_label='quiz', model='ruleexception')
    content_type = models.ForeignKey(
        ContentType,
        verbose_name='answer',
        limit_choices_to=limit,
        null=True,
        blank=True
    )
    object_id = models.PositiveIntegerField(
        verbose_name='related object',
        null=True
    )
    content_object = GenericForeignKey('content_type', 'object_id')

    question = models.ForeignKey(Question)

    def __str__(self):
        pass
