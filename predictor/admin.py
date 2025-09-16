from django.contrib import admin
from .models import PredictionHistory

@admin.register(PredictionHistory)
class PredictionHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "player_name",
        "league",
        "position",
        "age",
        "matches",
        "goals",
        "assists",
        "predicted_value",
        "created_at",
        "user",
    )
    list_filter = ("league", "position", "created_at")
    search_fields = ("player_name", "league", "position", "user__username")
    ordering = ("-created_at",)
