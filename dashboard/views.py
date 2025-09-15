from django.shortcuts import render
from predictor.models import PredictionHistory
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    predictions = PredictionHistory.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "dashboard/dashboard.html", {"predictions": predictions})
