from django.contrib import admin
from .models import Review

# Register your models here.
#admin.site.register(Lost)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass