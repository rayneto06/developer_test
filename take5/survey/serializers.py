from survey.models import Survey, SurveyQuestion, SurveyQuestionAlternative
from rest_framework import serializers

# https://www.django-rest-framework.org/topics/writable-nested-serializers/


class SurveyQuestionAlternativeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyQuestionAlternative
        fields = ['id', 'alternative']


class SurveyQuestionSerializer(serializers.ModelSerializer):

    alternatives = SurveyQuestionAlternativeSerializer(many=True, read_only=True)

    class Meta:
        model = SurveyQuestion
        fields = ['id', 'text', 'alternatives']


class SurveySerializer(serializers.ModelSerializer):

    questions = SurveyQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ['id', 'name', 'description', 'questions']
