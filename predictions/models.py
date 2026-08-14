from django.db import models


class Match(models.Model):
    match_id = models.IntegerField(unique=True, verbose_name="ID матча")
    home_team = models.CharField(max_length=255, verbose_name="Хозяева")
    away_team = models.CharField(max_length=255, verbose_name="Гости")
    home_score = models.PositiveIntegerField(null=True, blank=True, verbose_name="Голы хозяев")
    away_score = models.PositiveIntegerField(null=True, blank=True, verbose_name="Голы гостей")
    status = models.CharField(max_length=50, verbose_name="Статус")
    winner = models.CharField(max_length=50, null=True, blank=True, verbose_name="Победитель")
    statistics = models.JSONField(null=True, blank=True, verbose_name="Статистика")

    class Meta:
        verbose_name = "Матч"
        verbose_name_plural = "Матчи"

    def __str__(self):
        return f"{self.home_team} - {self.away_team}"
