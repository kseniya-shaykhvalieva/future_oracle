from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from .models import Match
from .services import get_prediction
from .serializers import MatchSerializer


class MatchPredictionView(RetrieveAPIView):
    queryset = Match.objects.all()
    lookup_field = 'match_id'

    def retrieve(self, request, *args, **kwargs):
        match = self.get_object()
        result = get_prediction(match.match_id)
        return Response(result)


class MatchListView(ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
