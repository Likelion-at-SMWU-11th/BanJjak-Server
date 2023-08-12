from django.contrib import admin
from .models import Request

# Register your models here.
#admin.site.register(Lost)

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    pass