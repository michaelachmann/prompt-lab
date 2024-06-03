from django.shortcuts import render, redirect, get_object_or_404
from .models import Prompt
from .forms import PromptForm
from django.contrib.auth.decorators import login_required


def prompt_list(request):
    prompts = Prompt.objects.all()
    return render(request, 'prompts/prompt_list.html', {'prompts': prompts})


def prompt_detail(request, pk):
    prompt = get_object_or_404(Prompt, pk=pk)
    return render(request, 'prompts/prompt_detail.html', {'prompt': prompt})

@login_required  # Ensures that only logged-in users can access this view
def prompt_create(request):
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.save(commit=False)  # Do not immediately save the form
            prompt.creator = request.user     # Set the creator to the current user
            prompt.last_modified_by = request.user
            prompt.save()                     # Now save it with the creator set
            return redirect('prompt_list')
    else:
        form = PromptForm()
    return render(request, 'prompts/prompt_form.html', {'form': form})

@login_required
def prompt_update(request, pk):
    prompt = get_object_or_404(Prompt, pk=pk)
    if request.method == 'POST':
        form = PromptForm(request.POST, instance=prompt)
        if form.is_valid():
            updated_prompt = form.save(commit=False)
            updated_prompt.last_modified_by = request.user  # Set the user who last modified the prompt
            updated_prompt.save()
            return redirect('prompt_list')
    else:
        form = PromptForm(instance=prompt)
    return render(request, 'prompts/prompt_form.html', {'form': form})

@login_required
def prompt_delete(request, pk):
    prompt = get_object_or_404(Prompt, pk=pk)
    if request.method == 'POST':
        prompt.delete()
        return redirect('prompt_list')
    return render(request, 'prompts/prompt_confirm_delete.html', {'prompt': prompt})
