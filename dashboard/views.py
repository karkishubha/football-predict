from django.shortcuts import render,redirect
from predictor.models import PredictionHistory
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from predictor.models import PredictionHistory
from predictor.forms import PredictionUpdateForm
import joblib, pandas as pd, os
from django.conf import settings

@login_required
def dashboard(request):
    predictions = PredictionHistory.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "dashboard/dashboard.html", {"predictions": predictions})

# load model once
model_path = os.path.join(settings.BASE_DIR, "predictor/model/market_value_model.pkl")
model = joblib.load(model_path)
expected_columns = list(model.feature_names_in_)


@login_required
def delete_prediction(request, pk):
    prediction = get_object_or_404(PredictionHistory, pk=pk, user=request.user)
    prediction.delete()
    return redirect("dashboard")


@login_required
def update_prediction(request, pk):
    prediction = get_object_or_404(PredictionHistory, pk=pk, user=request.user)

    if request.method == "POST":
        form = PredictionUpdateForm(request.POST, instance=prediction)
        if form.is_valid():
            updated = form.save(commit=False)

            # build feature dict (same as in predictor/views.py)
            data = {col: 0 for col in expected_columns}
            for col in ["Leauge", "Pos", "Nation"]:
                if col in data:
                    data[col] = ""

            if "MP" in data:
                data["MP"] = updated.matches
            if "Gls" in data:
                data["Gls"] = updated.goals
            if "Ast" in data:
                data["Ast"] = updated.assists
            if "Age" in data:
                data["Age"] = updated.age
            if "Leauge" in data:
                data["Leauge"] = updated.league
            if "Pos" in data:
                data["Pos"] = updated.position

            features_df = pd.DataFrame([data], columns=expected_columns)
            updated.predicted_value = model.predict(features_df)[0]

            updated.save()
            return redirect("dashboard")
    else:
        form = PredictionUpdateForm(instance=prediction)

    return render(request, "predictor/update_prediction.html", {
        "form": form,
        "prediction": prediction,
    })