from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Dataset
from .forms import DatasetForm
from django.http import JsonResponse
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

@login_required
def tag_list(request):
    datasets = Dataset.objects.values_list('tags', flat=True)
    tags = set()
    for dataset_tags in datasets:
        tags.update(tag.strip() for tag in dataset_tags.split(','))
    return JsonResponse(list(tags), safe=False)

@login_required
def dataset_list(request):
    datasets = Dataset.objects.all()
    return render(request, 'datasets/dataset_list.html', {'datasets': datasets})

@login_required
def dataset_detail(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    return render(request, 'datasets/dataset_detail.html', {'dataset': dataset})

@login_required
def dataset_create(request):
    if request.method == 'POST':
        form = DatasetForm(request.POST, request.FILES)
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.creator = request.user
            dataset.last_modified_by = request.user

            if request.FILES:
                file = request.FILES['file']
                dataset.size = file.size // 1024  # Größe in KB berechnen
                dataset.file = file

            dataset.save()
            return redirect('dataset_list')
    else:
        form = DatasetForm()
    return render(request, 'datasets/dataset_form.html', {'form': form})

@login_required
def dataset_update(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    if request.method == 'POST':
        form = DatasetForm(request.POST, request.FILES, instance=dataset)
        if form.is_valid():
            updated_dataset = form.save(commit=False)
            updated_dataset.last_modified_by = request.user

            if request.FILES:
                file = request.FILES['file']
                updated_dataset.size = file.size // 1024  # Größe in KB berechnen
                updated_dataset.file = file

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

class DatasetEditView(UpdateView):
    model = Dataset
    form_class = DatasetForm
    template_name = 'dataset_edit.html'  # Hier geben Sie den Namen Ihrer neuen Template-Datei an

    def get_success_url(self):
        return reverse_lazy('dataset_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context