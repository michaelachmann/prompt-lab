from django.shortcuts import render

# 2. Import Modules and models .
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MLmodel
from .forms import MLmodel_form

# 2a. Erstellen der View für das Anzeigen der Daten
def MLmodel_list(request):
    MLmodels = MLmodel.objects.all()
    return render(request, '/Users/leobru/PycharmProjects/prompt-lab/MLmodels/templates/MLmodels/MLmodels_list.html'. {'MLmodels': MLmodels})


# 3. Erstellen der View für das Hinzufügen neuer Daten
@login_required
def create_MLmodel(request):
    if request.method == 'POST':
        form = MLmodel_form(request.POST)
        if form.is_valid():
            mlmodel = form.save(commit=False)
            mlmodel.creator = request.user
            mlmodel.last_modified_by = request.user
            mlmodel.save()
            return redirect('MLmodel_list')
        else:
            form = MLmodel_form()
        return render(request, '/Users/leobru/PycharmProjects/prompt-lab/MLmodels/templates/MLmodels/MLmodel_form.html', {'form': form})


# 4. Erstellen der View für das Aktualisieren bestehender Daten

@login_required
def MLmodel_update(request, pk):
    MLmodel = get_object_or_404(MLmodel, pk=pk)
    if request.method == 'POST':
        form = MLmodel_form(request.POST, instance=mlmodel)
        if form.is_valid():
            updated_mlmodel = form.save(commit=False)
            updated_mlmodel.last_modified_by = request.user
            updated_mlmodel.save()
            return redirect('MLmodel_list')
        else:
            form = MLmodel_form(instance = mlmodel)
        return render(request, '/Users/leobru/PycharmProjects/prompt-lab/MLmodels/templates/MLmodels/MLmodel_form.html', {'form':form})

# 5. View für das Löschen von Dateien

@login_required()
def MLmodel_delete(request, pk):
    mlmodel = get_object_or_404(MLmodel, pk=pk)
    if request.method == 'POST':
        mlmodel.delete()
        return redirect('MLmodel_list')
    return render(request, '/Users/leobru/PycharmProjects/prompt-lab/MLmodels/templates/MLmodels/MLmodel_confirm_delete.html', {'mlmodel':mlmodel}))


