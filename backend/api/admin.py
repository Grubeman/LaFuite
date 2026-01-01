from django.contrib import admin

# Register your models here.
from .models.universe import Universe

admin.site.register(Universe)