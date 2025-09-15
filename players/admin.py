from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "player", "club", "league", "pos", "age", "mp", "goals", "assists", "market_value"
    )
    search_fields = ("player", "club", "league", "nation")
    list_filter = ("league", "pos", "nation")
    ordering = ("player",)
    list_per_page = 50

    # Optional: make fields read-only in admin if you don't want accidental edits
    # readonly_fields = ("player", "club", "league")
