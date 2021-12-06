from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Snack
# Register your models here.

# @admin.register(Snack)
class AdminSnack(admin.ModelAdmin):
  list_display = ['name', 'description', 'rating', 'purchaser']
  search_fields = ['name',]
  list_display_links = ('name', 'purchaser',)
  list_filter = ['purchaser']

admin.site.register(Snack, AdminSnack)