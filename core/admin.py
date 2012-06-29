from django import forms
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm

class FlatPageAdmin(admin.ModelAdmin):
	save_on_top = True
	pass

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)