from django.views.generic import TemplateView, DetailView
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


class MatchListAPIView(ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchListView(TemplateView):
    template_name = 'predictions/matches.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['matches'] = Match.objects.all()[:10]
        return context


class MatchDetailView(DetailView):
    model = Match
    template_name = 'predictions/match_detail.html'
    context_object_name = 'match'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prediction'] = get_prediction(self.object.match_id)
        return context
