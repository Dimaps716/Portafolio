from django.contrib import admin
from .models import project

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields =('created', 'updated')

# Register your models here.
admin.site.register(project, ProjectAdmin)