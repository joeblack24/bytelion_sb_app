from django.contrib import admin

# Register your models here.
from .models import BackScratchers, Size

@admin.register(BackScratchers)
class BackScratcherAdmin(admin.ModelAdmin):
    pass

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass
