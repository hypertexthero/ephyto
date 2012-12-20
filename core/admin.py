from django import forms
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm

# Make sites selected by default - http://stackoverflow.com/a/5669589/412329
from django.contrib.sites.models import Site
class FlatPageAdmin(admin.ModelAdmin):
	def formfield_for_manytomany(self, db_field, request=None, **kwargs):
            if db_field.name == "sites":
                kwargs["initial"] = [Site.objects.get_current()]
            return super(FlatPageAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
	
	exclude = ('enable_comments','template_name',)
	save_on_top = True
	pass

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)