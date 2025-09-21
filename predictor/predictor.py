import joblib
import pandas as pd
import os

# path to model
MODEL_PATH = os.path.join("model", "market_value_model.pkl")

# load model
model = joblib.load(MODEL_PATH)

# get expected columns from model
expected_columns = list(model.feature_names_in_)

def predict_market_value(player_name, league, position, age, matches, goals, assists):
    # initialize dict with 0
    data = {col: 0 for col in expected_columns}

    # categorical placeholders
    for col in ["Leauge", "Pos", "Nation"]:
        if col in data:
            data[col] = ""

    # fill user data
    if "MP" in data:
        data["MP"] = matches
    if "Gls" in data:
        data["Gls"] = goals
    if "Ast" in data:
        data["Ast"] = assists
    if "Age" in data:
        data["Age"] = age
    if "Leauge" in data:
        data["Leauge"] = league
    if "Pos" in data:
        data["Pos"] = position

    # build dataframe with correct column order
    features_df = pd.DataFrame([data], columns=expected_columns)

    # predict
    prediction = model.predict(features_df)[0]
    return round(float(prediction), 2)
