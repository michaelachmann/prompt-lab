from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MLModel
from .forms import MLModelForm

def ml_model_list(request):
    models = MLModel.objects.all()
    return render(request, '/templates/ml_models/ml_model_list.html', {'models': models})

@login_required
def ml_model_create(request):
    if request.method == 'POST':
        form = MLModelForm(request.POST)
        if form.is_valid():
            ml_model = form.save(commit=False)  # Do not immediately save the form
            ml_model.creator = request.user     # Set the creator to the current user
            ml_model.last_modified_by = request.user
            ml_model.save()                     # Now save it with the creator set
            return redirect('ml_model_list')
    else:
        form = MLModelForm()
    return render(request, 'templates/ml_models/prompt_form.html', {'form': form})

@login_required
def ml_model_update(request, pk):
    ml_model = get_object_or_404(MLModel, pk=pk)
    if request.method == 'POST':
        form = MLModelForm(request.POST, instance=ml_model)
        if form.is_valid():
            updated_ml_model = form.save(commit=False)
            updated_ml_model.last_modified_by = request.user  # Set the user who last modified the prompt
            updated_ml_model.save()
            return redirect('ml_model_list')
    else:
        form = MLModelForm(instance=ml_model)
    return render(request, 'templates/ml_models/ml_model_form.html', {'form': form})

@login_required
def ml_model_delete(request, pk):
    ml_model = get_object_or_404(MLModel, pk=pk)
    if request.method == 'POST':
        ml_model.delete()
        return redirect('ml_model_list')
    return render(request, 'templates/ml_models/ml_model_confirm_delete.html', {'models': models})


jhdfsfsd


