from django.contrib import admin

from .models import List, Item

admin.site.register(Item)
admin.site.register(List)

