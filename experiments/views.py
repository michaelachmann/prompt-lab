from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ExperimentForm
from .models import Experiment


# Create your views here.
def experiment_list(request):
    experiments = Experiment.objects.all()
    return render(request, 'experiments/experiments_list.html', {'experiments': experiments})


@login_required  # Ensures that only logged-in users can access this view
def experiment_create(request):
    if request.method == 'POST':
        form = ExperimentForm(request.POST)
        if form.is_valid():
            experiment = form.save(commit=False)  # Do not immediately save the form
            experiment.creator = request.user  # Set the creator to the current user
            experiment.last_modified_by = request.user
            experiment.save()  # Now save it with the creator set
            return redirect('experiment_list')
    else:
        form = ExperimentForm()
    return render(request, 'experiments/experiment_form.html', {'form': form})


@login_required
def experiment_update(request, pk):
    experiment = get_object_or_404(Experiment, pk=pk)
    if request.method == 'POST':
        form = ExperimentForm(request.POST, instance=experiment)
        if form.is_valid():
            updated_prompt = form.save(commit=False)
            updated_prompt.last_modified_by = request.user
            updated_prompt.save()  # Now save it with the creator set
            return redirect('experiment_list')
    else:
        form = ExperimentForm(instance=experiment)
    return render(request, 'experiments/experiment_form.html', {'form': form})

def experiment_delete(request):
    experiments = Experiment.objects.all()
    return render(request, 'experiments/experiments_list.html', {'experiments': experiments})


def experiment_detail(request, pk):
    experiment = get_object_or_404(Experiment, pk=pk)
    return render(request, 'experiments/experiment_detail.html', {'experiment': experiment})
