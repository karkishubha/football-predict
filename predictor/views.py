from django.shortcuts import render
from .forms import PlayerStatsForm
from players.models import Player
from .models import PredictionHistory   
import joblib
import pandas as pd
import os
from django.conf import settings



model_path = os.path.join(settings.BASE_DIR, "predictor/model/market_value_model.pkl")
model = joblib.load(model_path)

expected_columns = list(model.feature_names_in_)


def predict_form(request):
    predicted_value = None

    if request.method == "POST":
        form = PlayerStatsForm(request.POST)
        if form.is_valid():
            # Extract user inputs
            player_name = form.cleaned_data["player_name"]
            league = form.cleaned_data["league"]
            position = form.cleaned_data["position"]
            age = form.cleaned_data["age"]
            matches = form.cleaned_data["matches"]
            goals = form.cleaned_data["goals"]
            assists = form.cleaned_data["assists"]

            
            data = {col: 0 for col in expected_columns}

           
            for col in ['Leauge', 'Pos', 'Nation']:
                if col in data:
                    data[col] = ''

           
            if 'MP' in data:
                data['MP'] = matches
            if 'Gls' in data:
                data['Gls'] = goals
            if 'Ast' in data:
                data['Ast'] = assists
            if 'Age' in data:
                data['Age'] = age
            if 'Leauge' in data:
                data['Leauge'] = league
            if 'Pos' in data:
                data['Pos'] = position

           
            features_df = pd.DataFrame([data], columns=expected_columns)

            
            predicted_value = model.predict(features_df)[0]

            
            Player.objects.create(
                player=player_name,
                league=league,
                pos=position,
                age=age,
                mp=matches,
                goals=goals,
                assists=assists,
                market_value=predicted_value
            )

           
            if request.user.is_authenticated:
                PredictionHistory.objects.create(
                    user=request.user,
                    player_name=player_name,
                    league=league,
                    position=position,
                    age=age,
                    matches=matches,
                    goals=goals,
                    assists=assists,
                    predicted_value=predicted_value,
                )

    else:
        form = PlayerStatsForm()

    return render(request, "predictor/predict.html", {
        "form": form,
        "predicted_value": predicted_value
    })
