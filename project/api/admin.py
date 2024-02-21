from django.contrib import admin
from .models import Executor, Task

class ExecutorAdmin(admin.ModelAdmin) :
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class TaskAdmin(admin.ModelAdmin) :
    list_display = ('date_creation', 'executor', 'priority', 'header', 'comment')
    list_display_links = ('date_creation', 'executor', 'priority', 'header', 'comment')
    search_fields = ('date_creation', 'executor', 'priority', 'header', 'comment')

admin.site.register(Executor, ExecutorAdmin)
admin.site.register(Task, TaskAdmin)
