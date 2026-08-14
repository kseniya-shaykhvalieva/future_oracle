from .models import Match


def get_prediction(match_id):
    match = Match.objects.get(match_id=match_id)
    # Берем последние 5 матчей хозяев
    home_matches = Match.objects.filter(home_team=match.home_team, status='finished').order_by('-id')[:5]
    home_wins = sum(1 for m in home_matches if m.winner == 'home')

    # Берем последние 5 матчей гостей
    away_matches = Match.objects.filter(away_team=match.away_team, status='finished').order_by('-id')[:5]
    away_wins = sum(1 for m in away_matches if m.winner == 'away')

    confidence = round((home_wins / 5) * 100) if home_wins else 0
    prediction = "Победа хозяев" if home_wins > away_wins else "Ничья или гости"

    return {
        "match": str(match),
        "prediction": prediction,
        "confidence": confidence,
        "risk": "Высокий" if confidence < 50 else "Низкий"
    }
