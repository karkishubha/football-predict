import joblib
import pandas as pd
import os
from django.conf import settings

# Paths
MODEL_PATH = os.path.join(settings.BASE_DIR, "predictor", "model", "market_value_model.pkl")
FEATURES_PATH = os.path.join(settings.BASE_DIR, "predictor", "model", "features.pkl")


model_pipeline = joblib.load(MODEL_PATH)
features = joblib.load(FEATURES_PATH)

def predict_market_value(player_data: dict):
    """
    Takes a dictionary of player attributes and returns predicted market value.
    Example player_data = {"Age": 22, "Nation": "BRA", "Pos": "FW", ...}
    """
    df = pd.DataFrame([player_data])
    # Reorder columns to match training data
    df = df.reindex(columns=features, fill_value=0)
    prediction = model_pipeline.predict(df)
    return round(float(prediction[0]), 2)
