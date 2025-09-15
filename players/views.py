from django.shortcuts import render, get_object_or_404
from .models import Player
from django.db.models import Q # Import the Q object

def player_list(request):
    # Get all players
    players = Player.objects.all()

    # Get the search query from the URL (e.g., ?search=...)
    search_query = request.GET.get('search')

    # If a search query exists, filter the players
    if search_query:
        players = players.filter(
            Q(player__icontains=search_query) | 
            Q(club__icontains=search_query) |
            Q(nation__icontains=search_query)
        ).distinct()

    # Pass the filtered (or unfiltered) list of players to the template
    return render(request, "players/player_list.html", {"players": players})

# Detail view remains unchanged
def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, "players/player_detail.html", {"player": player})