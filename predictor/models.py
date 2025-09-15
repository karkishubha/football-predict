from django.db import models
from django.contrib.auth.models import User


class PredictionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="predictions")
    player_name = models.CharField(max_length=100)
    league = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    age = models.IntegerField()
    matches = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    predicted_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player_name} - {self.predicted_value}"
