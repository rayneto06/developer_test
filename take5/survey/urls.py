from django.urls import include, path
from rest_framework import routers
from survey import views

router = routers.DefaultRouter()
router.register(r'survey', views.SurveyViewSet)
router.register(r'questions', views.SurveyQuestionViewSet)
router.register(r'alternatives', views.SurveyQuestionAlternativeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
