from django.contrib import admin
from .models import Found

# Register your models here.
#admin.site.register(Lost)

@admin.register(Found)
class LostAdmin(admin.ModelAdmin):
    pass