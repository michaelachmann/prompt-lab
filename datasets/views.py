from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Dataset
from .forms import DatasetForm

def dataset_list(request):
    datasets = Dataset.objects.all()
    return render(request, 'datasets/dataset_list.html', {'datasets': datasets})

@login_required  # Ensures that only logged-in users can access this view
def dataset_create(request):
    if request.method == 'POST':
        form = DatasetForm(request.POST)
        if form.is_valid():
            dataset = form.save(commit=False)  # Do not immediately save the form
            dataset.creator = request.user     # Set the creator to the current user
            dataset.last_modified_by = request.user
            dataset.save()                     # Now save it with the creator set
            return redirect('dataset_list')
    else:
        form = DatasetForm()
    return render(request, 'datasets/dataset_form.html', {'form': form})

@login_required
def dataset_update(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    if request.method == 'POST':
        form = DatasetForm(request.POST, instance=dataset)
        if form.is_valid():
            updated_dataset = form.save(commit=False)
            updated_dataset.last_modified_by = request.user  # Set the user who last modified the prompt
            updated_dataset.save()
            return redirect('dataset_list')
    else:
        form = DatasetForm(instance=dataset)
    return render(request, 'datasets/dataset_form.html', {'form': form})


@login_required
def dataset_delete(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    if request.method == 'POST':
        dataset.delete()
        return redirect('dataset_list')
    return render(request, 'datasets/dataset_confirm_delete.html', {'dataset': dataset})
# Create your views here.
