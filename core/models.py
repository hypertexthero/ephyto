# from django.db import models
# from django.contrib.sites.models import Site
# # http://stackoverflow.com/questions/1021487/add-functionality-to-django-flatpages-without-changing-the-original-django-app
# from django.contrib.flatpages.models import FlatPage as FlatPageOld
# 
# class FlatPage(FlatPageOld):
#     # order = models.PositiveIntegerField(unique=True)
#     sites = models.ManyToManyField(Site, default=Site.objects.get_current())