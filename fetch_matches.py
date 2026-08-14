import os
import django
import requests
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from predictions.models import Match

url = "https://api.api-sport.ru/v2/ice-hockey/matches?tournament_id=268"

headers = {"Authorization": settings.API_KEY}
response = requests.get(url, headers=headers)
data = response.json()

for match in data.get("matches", []):
    Match.objects.update_or_create(
        match_id=match["id"],
        defaults={
            "home_team": match["homeTeam"]["name"],
            "away_team": match["awayTeam"]["name"],
            "home_score": match.get("homeScore", {}).get("current"),
            "away_score": match.get("awayScore", {}).get("current"),
            "status": match.get("status"),
            "winner": match.get("winner"),
            "statistics": match.get("matchStatistics"),
        }
    )

print("Данные сохранены")
