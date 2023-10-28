from django.contrib import admin

# Register your models here.

from .models import User, Exercise, WorkPlan

admin.site.register(User)
admin.site.register(Exercise)
admin.site.register(WorkPlan)
