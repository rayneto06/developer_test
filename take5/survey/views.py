from rest_framework import viewsets
from rest_framework import permissions
from survey.serializers import SurveySerializer, SurveyQuestionSerializer, SurveyQuestionAlternativeSerializer
from survey.models import Survey, SurveyQuestion, SurveyQuestionAlternative

# Create your views here.


class SurveyViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Survey.objects.prefetch_related('questions__alternatives')
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticated]


class SurveyQuestionViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SurveyQuestion.objects.prefetch_related('alternatives')
    serializer_class = SurveyQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class SurveyQuestionAlternativeViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SurveyQuestionAlternative.objects.all()
    serializer_class = SurveyQuestionAlternativeSerializer
    permission_classes = [permissions.IsAuthenticated]
