from django import forms
import math


LEAGUE_ARRAY = ['Ligue1', 'Premier League', 'Bundesliga', 'La Liga', float('nan'), 'Serie A']
LEAGUE_CHOICES = [(league, league) for league in LEAGUE_ARRAY if not (isinstance(league, float) and math.isnan(league))]


POSITION_ARRAY = ['FW', 'MF,FW', 'MF', 'DF', float('nan'), 'MF,DF', 'WB', 'DF,MF']
POSITION_CHOICES = [(pos, pos) for pos in POSITION_ARRAY if not (isinstance(pos, float) and math.isnan(pos))]

class PlayerStatsForm(forms.Form):
    player_name = forms.CharField(label="Player Name", max_length=100)
    league = forms.ChoiceField(label="League", choices=LEAGUE_CHOICES)
    position = forms.ChoiceField(label="Position", choices=POSITION_CHOICES)
    age = forms.IntegerField(label="Age")
    matches = forms.IntegerField(label="Matches Played")
    goals = forms.IntegerField(label="Goals")
    assists = forms.IntegerField(label="Assists")
