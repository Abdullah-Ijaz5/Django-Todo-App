from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm


def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added.')
            return redirect('home')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    return render(request, 'DjangoApp/home.html', {'tasks': tasks, 'form': form})


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('home')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, 'Task deleted.')
    return redirect('home')


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated.')
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'DjangoApp/edit_task.html', {'form': form, 'task': task})