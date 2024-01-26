from django.contrib import admin

from item import models

admin.site.register(models.Category)
admin.site.register(models.Item)