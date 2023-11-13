from django.shortcuts import render, redirect
from .models import Exercise
from .forms import ExerciseForm

# Create your views here.


from .models import User, Exercise, WorkPlan

def list_users(request):
    users = User.objects.all()
    return render(request, 'list_users.html', {'users': users})

def list_exercises(request):
    exercises = Exercise.objects.all()
    return render(request, 'list_exercises.html', {'exercises': exercises})

def list_workplans(request):
    workplans = WorkPlan.objects.all()
    return render(request, 'list_workplans.html', {'workplans': workplans})

def home(request):
    return render(request, 'home.html')

def new_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    return render(request, 'new_exercise.html', {'form': form})