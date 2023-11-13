from django.db import models

# User model
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

# Exercise model
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=100)
    description = models.TextField()
    sets = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return self.name

# WorkPlan model
class WorkPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return f"Workout Plan for {self.user.name}"
