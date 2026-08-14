from django.urls import path
from predictions.apps import PredictionsConfig
from predictions.views import MatchPredictionView, MatchListView

app_name = PredictionsConfig.name

urlpatterns = [
    path('predict/<int:match_id>/', MatchPredictionView.as_view(), name='predict'),
    path('matches/', MatchListView.as_view(), name='matches'),
]
