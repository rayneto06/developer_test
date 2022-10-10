from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Survey(models.Model):

    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)

    def __str__(self) -> str:
        return f'{self.name}'


class SurveyQuestion(models.Model):

    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=False)

    def __str__(self) -> str:
        return f'{self.text}'


class SurveyQuestionAlternative(models.Model):

    survey = models.ForeignKey(Survey, related_name='survey_alternatives', on_delete=models.CASCADE)
    question = models.ForeignKey(SurveyQuestion, related_name='alternatives', on_delete=models.CASCADE)
    alternative = models.CharField(max_length=255, blank=False)

    def __str__(self) -> str:
        return f'{self.alternative}'


class SurveyUserAnswer(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, related_name='survey_answer', on_delete=models.CASCADE)
    question = models.ForeignKey(SurveyQuestion, related_name='answer', on_delete=models.CASCADE)
    choice = models.ForeignKey(SurveyQuestionAlternative, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.choice}'
