from django.contrib import admin
from .models import Lost

# Register your models here.
#admin.site.register(Lost)

@admin.register(Lost)
class LostAdmin(admin.ModelAdmin):
    pass