from django.shortcuts import render
from .models import Experiment

# Create your views here.
def experiment_list(request):
    experiments = Experiment.objects.all()
    return render(request, 'experiments/experiments_list.html', {'experiments': experiments})