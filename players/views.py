from django.shortcuts import render, get_object_or_404
from .models import Player
from django.db.models import Q # Import the Q object

def player_list(request):
    # Get all players
    players = Player.objects.all()

   
    search_query = request.GET.get('search')


    if search_query:
        players = players.filter(
            Q(player__icontains=search_query) | 
            Q(club__icontains=search_query) |
            Q(nation__icontains=search_query)
        ).distinct()

    
    return render(request, "players/player_list.html", {"players": players})


def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, "players/player_detail.html", {"player": player})