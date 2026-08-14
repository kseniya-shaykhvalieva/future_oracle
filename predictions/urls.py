from django.urls import path
from predictions.apps import PredictionsConfig
from predictions.views import MatchPredictionView, MatchListAPIView, MatchListView, MatchDetailView

app_name = PredictionsConfig.name

urlpatterns = [
    path('predict/<int:match_id>/', MatchPredictionView.as_view(), name='predict'),
    path('matches/', MatchListAPIView.as_view(), name='matches'),
    path('', MatchListView.as_view(), name='match_list'),
    path('match/<int:pk>/', MatchDetailView.as_view(), name='match_detail'),
]
