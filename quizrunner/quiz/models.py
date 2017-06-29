from django.db import models


class Rule(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300)

    def __str__(self):
        return '({name}, {description})'.format(
            name=self.name,
            description=self.description
        )


class RuleException(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)

    def __str__(self):
        return '({name}, {description}, {rule})'.format(
            name=self.name,
            description=self.description,
            rule=self.rule.name
        )
