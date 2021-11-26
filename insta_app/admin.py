from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import insta_model, insta_ghost_model

admin.site.register(insta_model)

admin.site.register(insta_ghost_model)